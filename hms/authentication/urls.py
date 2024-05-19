from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("login/", views.CustomAuthToken.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout")
]

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='user')
urlpatterns += router.urls