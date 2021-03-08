from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegisterForm, LoginForm, EmailVerificationForm
from .tasks import send_email_confirmation_task
from .services import (
    create_email_verification_code,
    compare_verification_code,
    verify_email,
)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "authentication/register.html", {"form": form})

    def post(self, request):
        context = {}
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            raw_password = form.cleaned_data.get("password")
            user_obj = authenticate(
                request, email=user.email, password=raw_password
            )
            if user is not None:
                login(request, user_obj)
                code = create_email_verification_code(user.email)
                send_email_confirmation_task.delay(user.email, code)
                return redirect("auth:email_verification")
        context["form"] = form
        return render(request, "authentication/register.html", context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "authentication/login.html", {"form": form})

    def post(self, request):
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(
                username=credentials["email"], password=credentials["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("auth:email_verification")
        context["form"] = form
        return render(request, "authentication/login.html", context)


class EmailVerificationView(View):
    def get(self, request):
        form = EmailVerificationForm()
        return render(
            request, "authentication/email_verification.html", {"form": form}
        )

    def post(self, request):
        context = {}
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            code = credentials.get("verification_code")
            email = request.user.email
            if compare_verification_code(email, code):
                verify_email(email)
                return redirect("auth:login")
            else:
                context["verification_failed"] = True
        context["form"] = form
        return render(
            request, "authentication/email_verification.html", context
        )
