from django.urls import path

from .views import *

urlpatterns = [
    path('start/<str:topic>/<int:user_id>', ChatView.as_view(), name='chat-start-view'),
    path('reply/', ChatListView.as_view(), name='chat-reply-view'),
]