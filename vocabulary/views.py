from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import vocaSerializer
from .models import Vocabulary


class VocaList(APIView):

    def get(self, request):
        user_id = request.GET.get('id')
        queryset = Vocabulary.objects.filter(user_id=user_id)
        serializer = vocaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        voca = vocaSerializer(data=request.data)
        print(voca)
        if voca.is_valid():
            voca.save()
            return Response(voca.data)
        return Response(voca.errors, status=status.HTTP_400_BAD_REQUEST)
