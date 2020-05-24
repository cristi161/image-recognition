from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #  < h1 > sfsafas < / h1 >
    #  < form
    # method = "POST"
    # action = "" >
    # { % csrf_token %}
    # {{form2.username.label}}
    # {{form2.username}}

    # {form2.email.label}}
    # {{form2.email}}

    # {{form2.password1.label}}
    # {{form2.password1}}

    # {{form2.password2.label}}
    # {{form2.password2}}

    # < input
    # type = "submit"
    # name = "Create User" >

    # < / form >
