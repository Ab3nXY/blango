import logging
from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm 
from django.utils import timezone


logger = logging.getLogger(__name__)


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info(
                    "Created comment on Post %d for user %s", post.pk, request.user
                )

                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
      request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
      )

from django.contrib import messages

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
        request, "blog/post-detail.html", {"post_list_url": reverse("post-list")}
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