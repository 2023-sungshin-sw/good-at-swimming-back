from rest_framework import serializers
from .models import Vocabulary


class vocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'
