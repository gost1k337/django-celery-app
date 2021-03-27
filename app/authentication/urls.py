from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from .views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet, basename='user')

app_name = 'auth'
urlpatterns = [
    *router.urls,
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
]
