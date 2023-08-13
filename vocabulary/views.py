from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import vocaSerializer
from .models import Vocabulary

class VocaView(APIView):
    def get_by_user(self, request):
        user_id = request.GET.get('id')
        print(user_id)
        queryset = Vocabulary.objects.filter(user_id=user_id)
        serializer = vocaSerializer(queryset, many=True)
        return Response(serializer.data)


