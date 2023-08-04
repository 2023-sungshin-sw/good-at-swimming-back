from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import userSerializer
from .models import User

"""https://velog.io/@dbstjd0924/django-mysql-restful-api-%EB%A7%8C%EB%93%A4%EA%B8%B0"""


@api_view(['GET'])
def getUser(request):
    queryset = User.objects.all()
    serializer = userSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postUser(request):
    user = userSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
