from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'usernameInput', 'placeholder': 'Username...'})
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'emailInput', 'placeholder': 'Email...'})
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'passwordInput', 'placeholder': 'Password...'})
    )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'emailInput', 'placeholder': 'Email...'})
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'passwordInput', 'placeholder': 'Password...'})
    )
