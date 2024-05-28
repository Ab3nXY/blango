from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User  # Import the User model
from django.contrib import messages  # for adding messages

@login_required
def profile(request):
  if request.method == 'POST':
    user = request.user
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    try:
      user.save()
      messages.success(request, 'Your profile has been updated successfully!')
      return redirect('index')
    except Exception as e:
      messages.error(request, f'An error occurred: {e}')  # Add specific error message
  else:
    user = request.user

  context = {'user': user}
  return render(request, "blango_auth/profile.html", context)
