from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import userSerializer
from .models import User

"""https://velog.io/@dbstjd0924/django-mysql-restful-api-%EB%A7%8C%EB%93%A4%EA%B8%B0"""


class UserView(APIView):
    def get(self):
        queryset = User.objects.all()
        serializer = userSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        user = userSerializer(data=request.data)
        print(user)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
