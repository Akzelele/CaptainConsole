from django.forms import ModelForm
from django.forms import widgets
from django import forms
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')


class EditProfileForm(UserChangeForm):
        class Meta:
            model = User
            fields = (
                'email',
                'username',
                'first_name',
                'last_name',
                'password'
            )







