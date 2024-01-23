from .views import *
from django.urls import path


urlpatterns = [
    path('/', main,name='home'),
    path('choice', choice,name='choice'),
    path('change', change,name='change'),

    ]