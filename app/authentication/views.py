from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import User
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        context = {}
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            if user is not None:
                return redirect('home:index')
        context['form'] = form
        return render(request, 'authentication/register.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(email=credentials['email'],
                                password=credentials['password'])
            if user is not None:
                login(request, user)
                return redirect('home:index')
        context['form'] = form
        return redirect('auth:login')
