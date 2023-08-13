from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import JsonResponse

from .serializers import *
from .models import *


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


class MeaningView(APIView):

    # 단어 뜻 리턴(단어 시험 중 단어의 의미가 궁금할때 이를 리턴하는 기능)
    def get(self, request):
        voca_id = request.GET.get('id')
        queryset = Vocabulary.objects.get(voca_id=voca_id)
        serializer = meaningSerializer(queryset)
        return Response(serializer.data)


class VocaTestCheckList(APIView):

    def post(self, request, type):
        voca_id = request.data['voca']
        data = {'state': 'fail', 'message': '실패하였습니다.'}
        if type == 'check':
            Vocabulary.objects.get(voca_id=voca_id).delete()
            data['state'] = 'success'
            data['message'] = '통과한 단어 삭제'
            return Response(data, status=status.HTTP_200_OK)
        elif type == 'xbutton':
            exam = examSerializer(data=request.data)
            if exam.is_valid():
                exam.save()
                data['state'] = 'success'
                data['message'] = '틀린 단어 테이블에 저장'
                return Response(data, status=status.HTTP_200_OK)

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

class VocaTestResultList(APIView):

    def get(self, request):
        user_id = request.GET.get('id')

        # 시험 후 xbutton을 누른 모르는 단어들을 가져온다.
        queryset = Exam.objects.filter(voca__user_id=user_id)
        exams_data = examSerializer(queryset, many=True).data
        queryset.delete() # 모르는 단어가 무엇인지 알게되면 exam table에서 삭제 -> 이후에는 필요없는 정보이기 때문이다.

        #모르는 단어들의 세부 정보를 가져온다.
        vocab_ids = [exam['voca'] for exam in exams_data]
        vocabularies = Vocabulary.objects.filter(voca_id__in=vocab_ids)
        vocab_data = vocaSerializer(vocabularies, many=True).data

        output_json = {
            'score': 20 - len(exams_data),
            'data': vocab_data
        }
        return Response(output_json)
