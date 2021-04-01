from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":    # Check if form is filled out/submitted
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()     # Save new user
            username = form.cleaned_data.get('username')
            # Flash message
            messages.success(
                request, f'Account created for {username}! You can now log in')
            return redirect('login')  # Redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# add decorator to require users to be logged in to see page. Redirects to login page (LOGIN_URL in settings)
@login_required
def profile(request):
    return render(request, 'users/profile.html')


""" 
Example of some FLASH messages for reference:

messages.debug
messages.info
messages.success
messages.warning
messages.error
"""
