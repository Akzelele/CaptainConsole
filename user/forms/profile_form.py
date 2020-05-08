from django.forms import ModelForm
from django.forms import widgets
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
