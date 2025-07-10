from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


#modify/add new attributes 

class RegisterForm (UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        # username, password1, password2 are bultin in Django, we add Email as extra field
        #layout of the fields where to be
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']