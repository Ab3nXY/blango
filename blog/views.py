import logging
from django.utils import timezone
from blog.models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm 
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import transaction
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})
    

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')  # Order comments by creation date descending
    comment_form = CommentForm(request.POST or None)

    if request.method == "POST" and comment_form.is_valid():
        with transaction.atomic():
            comment = comment_form.save(commit=False)
            comment.content_object = post
            comment.creator = request.user
            try:
                comment.sentiment = classify_comment(comment.content)
            except Exception as e:
                logger.error("Error classifying comment sentiment: %s", e)
                if request.is_ajax():
                    return JsonResponse({'error': 'Failed to analyze comment sentiment. Please try again.'}, status=500)
                messages.error(request, "Failed to analyze comment sentiment. Please try again.")
            comment.save()
            logger.info(
                "Created comment on Post %d for user %s with sentiment %s",
                post.pk, request.user, comment.sentiment
            )
            if request.is_ajax():
                return JsonResponse({
                    'creator': comment.creator.first_name,
                    'created_at': comment.created_at.strftime("%b, %d %Y %I:%M %p"),
                    'content': comment.content,
                    'sentiment': comment.sentiment,
                })
            return redirect(request.path_info)

    return render(request, "blog/post-detail.html", {"post": post, "comments": comments, "comment_form": comment_form})

@require_POST
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        try:
            comment.sentiment = classify_comment(comment.content)
        except Exception as e:
            logger.error("Error classifying comment sentiment: %s", e)
            return JsonResponse({'error': 'Failed to analyze comment sentiment. Please try again.'}, status=500)
        comment.save()
        
        # Return newly added comment details via AJAX response
        return JsonResponse({
            'creator': comment.creator.first_name,
            'created_at': comment.created_at.strftime("%b, %d %Y %I:%M %p"),
            'content': comment.content,
            'sentiment': comment.sentiment,
        })
    else:
        return JsonResponse({'errors': form.errors}, status=400)
    

@require_POST
@login_required
def delete_comment(request, comment_id):
    try:
        comment_to_delete = get_object_or_404(Comment, id=comment_id, creator=request.user)
        comment_to_delete.delete()
        return JsonResponse({'success': 'Comment deleted successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def delete_blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('index')  # Redirect to index page or any other page
    return render(request, 'blog/post-detail.html', {'post': post})


def post_table(request):
    return render(
        request, "blog/post-table.html", {"post_list_url": reverse("post-list")}
    )

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the current user as the author
            post.save()
            return redirect('blog-post-detail', slug=post.slug)  # Redirect to post detail page
    else:
        initial_data = {'author': request.user, 'published_at': timezone.now()}
        form = PostForm(initial=initial_data)
    return render(request, 'blog/create_blog.html', {'form': form})


from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Access the API key and service URL from the environment
api_key = os.getenv('IBM_WATSON_API_KEY')
service_url = os.getenv('IBM_WATSON_SERVICE_URL')

# Validate API key and service URL
if not api_key:
    raise ValueError("IBM_WATSON_API_KEY environment variable is not set")
if not service_url:
    raise ValueError("IBM_WATSON_SERVICE_URL environment variable is not set")

# Initialize the authenticator and the Natural Language Understanding client
authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

# Set the service URL
natural_language_understanding.set_service_url(service_url)

def classify_comment(comment):
    """
    Classifies a comment into positive, negative, or neutral sentiment using IBM Watson Natural Language Understanding.

    Args:
        comment_text: The text of the comment to classify.

    Returns:
        A dictionary containing the classification results, or None if an error occurs.
    """
    try:
        logger.debug(f"Classifying comment: {comment}")
        response = natural_language_understanding.analyze(
            text=comment,
            features=Features(sentiment=SentimentOptions())
        ).get_result()
        logger.debug(f"Watson NLU response: {response}")

        if 'sentiment' in response:
            sentiment = response['sentiment']['document']['score']
            if sentiment > 0.05:
                return 'positive'
            elif sentiment < -0.05:
                return 'negative'
            else:
                return 'neutral'
        else:
            logger.error("Sentiment analysis failed, no sentiment found in response")
            return None
    except Exception as e:
        logger.error(f"Error classifying comment: {e}")
        return None

