from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import userSerializer
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class JoinVIew(APIView):
    def post(self, request):
        user = userSerializer(data=request.data)
        if user.is_valid():
            user.save()
            output_json = {'state': 'success', 'message': '회원가입 성공', 'user_id': user.data["user_id"]}
            return Response(output_json, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        try:
            user = User.objects.get(phone=phone, password=password)
        except ObjectDoesNotExist:
            output_json = {'state': 'fail', 'message': '존재하지 않는 회원입니다.'}
            return Response(output_json, status=status.HTTP_400_BAD_REQUEST)

        serializer = userSerializer(user).data
        output_json = {'state': 'success', 'message': '로그인 성공', 'user_id': serializer['user_id']}
        return Response(output_json, status=status.HTTP_200_OK)


class PhoneCheckView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        output_json = {'is_valid': False, 'message': '중복된 아이디 입니다.'}
        try:
            User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            output_json['is_valid'] = True
            output_json['message'] = '사용 가능한 아이디 입니다.'

        return Response(output_json, status=status.HTTP_200_OK)
