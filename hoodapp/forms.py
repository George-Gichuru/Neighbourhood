from django import forms
from django.contrib.auth.models import User
from .models import Profile, Hood, Business, News
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=80)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)



class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'location')

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('owner', 'hood')

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ('admin',)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('user', 'hood')