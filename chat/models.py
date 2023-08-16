from django.db import models

from user.models import User


class ChatRoom(models.Model):
    chat_room_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    topic = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'chat_room'


class Chat(models.Model):
    chat_id = models.BigAutoField(primary_key=True)
    chat_room = models.ForeignKey(ChatRoom, models.DO_NOTHING)
    is_answer = models.BooleanField()
    is_send = models.BooleanField()
    message = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'chat'
