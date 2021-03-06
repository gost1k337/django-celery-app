from django.urls import path

from .views import RegisterView, LoginView, EmailVerificationView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('email_verification/', EmailVerificationView.as_view(), name='email_verification'),
]
