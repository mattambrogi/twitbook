# accounts/urls.py
from django.urls import path
from .views import SignUpView, ProfileView, UserListView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/profile', ProfileView.as_view(), name='profile'),
    path('<int:pk>/profile_update', ProfileUpdateView.as_view(), name='profile_update'),
    path('users/',UserListView.as_view(), name='user_list')
]