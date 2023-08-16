from rest_framework import serializers
from .models import *


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class chatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
