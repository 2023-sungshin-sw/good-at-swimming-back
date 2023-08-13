from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import vocaSerializer
from .models import Vocabulary


class VocaList(APIView):

    # 단어 리스팅
    def get(self, request):
        user_id = request.GET.get('id')
        queryset = Vocabulary.objects.filter(user_id=user_id)
        serializer = vocaSerializer(queryset, many=True)
        return Response(serializer.data)

    # 단어 저장
    def post(self, request):
        voca = vocaSerializer(data=request.data)
        if voca.is_valid():
            voca.save()
            return Response(voca.data)
        return Response(voca.errors, status=status.HTTP_400_BAD_REQUEST)


class VocaTestList(APIView):

    # 저장된 단어 중 랜덤으로 20개를 가져와 시험 단어 세트 리스팅
    def get(self, request):
        user_id = request.GET.get('id')
        queryset = Vocabulary.objects.filter(user_id=user_id).order_by('?')[:20]
        serializer = vocaSerializer(queryset, many=True)
        return Response(serializer.data)




