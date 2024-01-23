from . import  views
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('logout', my_logout, name='logout'),
    path('register', register, name='register'),
]