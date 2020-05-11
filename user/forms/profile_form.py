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
        exclude = [ 'id', 'user' ]
        widgets = {
            'profile_image': widgets.TextInput(attrs={ 'class' : 'form-control'})
        }


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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

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

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user