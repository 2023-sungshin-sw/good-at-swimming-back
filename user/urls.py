# user/urls.py
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('join/', JoinVIew.as_view()),
    path('login/', LoginView.as_view()),
    path('check-phone/', PhoneCheckView.as_view()),
]