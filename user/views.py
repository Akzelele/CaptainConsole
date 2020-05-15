from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from user.forms.profile_form import ProfileForm, EditProfileForm, RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from user.models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome Aboard {username}!')
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', {'form': form})


def profile(request):
    args = {'user': request.user}
    return render(request, 'user/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Profile edited successfully!')
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, f'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })


def edit_profile_picture(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, files=request.FILES, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f'Your picture was successfully updated!')
            return redirect('profile')
    return render(request, 'user/change_profile_picture.html', {
        'form': ProfileForm(instance=profile)
    })


def search_history(request):
    return render(request, 'user/search_history.html')
