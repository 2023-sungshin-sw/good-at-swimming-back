from django.urls import path

from .views import *

urlpatterns = [
    path('start/<str:topic>/<int:user_id>', ChatStartView.as_view(), name='chat-start-view'),
    path('reply/', ChatSaveView.as_view(), name='chat-reply-view'),
    path('feedback/<int:chat_room_id>', FeedbackList.as_view(), name='chat-feedback-view'),
]