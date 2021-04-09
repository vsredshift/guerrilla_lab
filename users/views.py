from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


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


# add decorator to require users to be logged in to see page. Redirects to login page (set LOGIN_URL in settings)
@login_required
def profile(request):
    if request.method == "POST":    # Populate forms with current user's data and check that form ready for submission
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        # Save only if valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(
                request, f'Your account has been successfully updated')
            return redirect('profile')  # Redirect to profile page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'users/profile_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(
            *args, **kwargs)
        target_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['target_user'] = target_user
        return context


""" 
Example of some FLASH messages for reference:
--------------------------------------------
messages.debug
messages.info
messages.success
messages.warning
messages.error
"""
