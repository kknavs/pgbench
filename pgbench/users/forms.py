from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegistationForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError('Username too short', code='message_too_short')
        elif User.objects.filter(username=username).exists():
            raise forms .ValidationError('Username already taken', code='username_taken')
        return username

    def clean_password2(self):
        password = self.cleaned_data.get("password", "")
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("Passwords don't match", code='passwords_dont_match')
        return password

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
