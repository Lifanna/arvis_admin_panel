from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('registration/', views.CustomRegistrationView.as_view(), name='registration'),
    path('users/', views.UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>', views.CustomUserUpdateView.as_view(), name='users-update'),
    path('users/delete/<int:pk>', views.CustomUserDeleteView.as_view(), name='users-update'),
]
