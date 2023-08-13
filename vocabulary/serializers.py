from rest_framework import serializers
from .models import *


class vocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'


class meaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ('voca_id', 'word', 'meaning')


class examSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'