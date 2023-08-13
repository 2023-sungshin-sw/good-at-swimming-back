from rest_framework import serializers
from .models import User  # serializer 관련 모듈과 모델을 import

"""
Serializer 란?
장고 모델 데이터를 JSON 타입으로 바꿔주는 작업을 해준다.
이를 직렬화라고 한다.
장고 모델 데이터를 템플릿에 뿌려주면 웹에 보여지듯, JSON 타입으로 뿌려주면 api로 통신이 되는 것이다.
장고 모델 데이터를 JSON 타입으로 바꿔주는 기계라고 이해하자.
"""


# 모델 데이터가 주어지면 fields 내용을 포함한 JSON 데이터로 변환해주는 Serializer가 완성
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('name', 'phone', 'password')

