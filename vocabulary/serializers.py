from rest_framework import serializers
from .models import Vocabulary


class vocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'


class meaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ('voca_id', 'word', 'meaning')
