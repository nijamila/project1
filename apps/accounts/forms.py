from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class PhoneVerificationForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'placeholder': 'Verification code', 'class': 'auth-input'})
    )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone',
            'class': 'auth-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'auth-input'
        })
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'age', 'phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']

        self.fields['phone'].required = True
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Phone number',
            'class': 'auth-input'
        })

        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'auth-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password', 'class': 'auth-input'})


class PhoneForm(forms.Form):
    phone = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'auth-input'})
    )



class CompleteSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'age', 'password1', 'password2']
