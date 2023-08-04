# user/urls.py
from django.contrib import admin
from django.urls import path

from .views import getUser, postUser

urlpatterns = [
    path('', getUser),
    path('', postUser),
    ]