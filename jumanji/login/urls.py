from django.contrib.auth.views import LogoutView
from django.urls import path

from login.views import LoginUserView, RegisterUserView, ProfileView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
]
