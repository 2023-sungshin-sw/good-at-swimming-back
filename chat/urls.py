from django.urls import path

from .views import *

urlpatterns = [
    path('<str:topic>/<int:user_id>', ChatView.as_view(), name='chat-start-view'),
]