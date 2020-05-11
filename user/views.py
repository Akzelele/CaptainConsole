from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from user.forms.profile_form import ProfileForm, EditProfileForm, RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from user.models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': RegistrationForm()
    })

def profile(request):
    args = {'user': request.user}
    return render(request, 'user/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(profile)

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
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
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
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/change_profile_picture.html', {
        'form': ProfileForm(instance=profile)
    })