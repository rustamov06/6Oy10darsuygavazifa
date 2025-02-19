from django import forms
from .models import Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    text = forms.CharField(required=False)
    widgets = {
        'text': forms.TextInput(attrs={'class': 'form-control'}),
    }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "form2Example11",
        "placeholder": "Username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "form2Example22",
        "placeholder": "Password"
    }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg",
        "id": "form3Example4cg"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-lg",
        "id": "form3Example4cdg"
    }))

    # Qo‘shimcha Profile maydonlari
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control form-control-lg"
    }))
    profession = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Kasbingiz"
    }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Manzil"
    }))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Telefon raqamingiz"
    }))
    site = forms.URLField(required=False, widget=forms.URLInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Shaxsiy sayt"
    }))
    github = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "GitHub profil"
    }))
    telegram = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Telegram username"
    }))
    instagram = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Instagram username"
    }))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "Facebook profil"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            "username": forms.TextInput(attrs={
                'class': "form-control form-control-lg",
                'id': "form3Example1cg"
            }),
            "email": forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'id': "form3Example3cg"
            })
        }

