from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from .talkgenerater import *


class ChatStartView(APIView):

    # 질문 5개 전달
    def get(self, request, topic, user_id):
        # 입력받은 정보 바탕으로 채팅방 생성
        input_data = {'topic': topic, 'user': user_id}
        chat_room_serializer = chatRoomSerializer(data=input_data)
        if chat_room_serializer.is_valid():
            chat_room_instance = chat_room_serializer.save()
            chat_room_id = chat_room_instance.chat_room_id

            # 토픽에 관련된 문장 5개 생성
            questions_dict = TalkGenerator.start(self, topic)
            for k, q in questions_dict.items():
                msg = {"chat_room": chat_room_id, "is_answer": False, "message": q}
                new_chat_serializer = messageSerializer(data=msg)
                if new_chat_serializer.is_valid():
                    new_chat_serializer.save()
                else:
                    return Response(new_chat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            output_json = {"chat_room_id": chat_room_id, "questions": questions_dict}
            return Response(output_json, status=status.HTTP_200_OK)
        else:
            return Response(chat_room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatSaveView(APIView):

    #1. 답변 채팅 저장
    #2. 답변에 대한 피드백 저장
    def post(self, request):
        # 1. 입력 받은 대답 채팅에 저장
        input_json = dict(request.data)
        input_json["is_answer"] = True
        input_json["is_send"] = True
        new_chat = messageSerializer(data=input_json)
        if new_chat.is_valid():
            new_chat.save()
        else:
            return Response(new_chat.errors, status=status.HTTP_400_BAD_REQUEST)

        # 2. 입력 받은 대답을 평가해 피드백에 저장
        feedback_msg = TalkGenerator.reply(self, input_json["message"])
        curr_chat_room = ChatRoom.objects.get(chat_room_id=input_json["chat_room"])
        user_id = curr_chat_room.user_id
        topic = curr_chat_room.topic
        feedback_json = {"user": user_id, "topic": topic, "original_sentence": input_json["message"],
                         "fix_sentence": feedback_msg}
        new_feedback = feedbackSerializer(data=feedback_json)
        if new_feedback.is_valid():
            new_feedback.save()
        else:
            return Response(new_feedback.errors, status=status.HTTP_400_BAD_REQUEST)
        data = {'state': 'success', 'message': '성공하셨습니다.'}
        return Response(data, status=status.HTTP_201_CREATED)


class FeedbackList(APIView):
    def get(self, request, chat_room_id):
        curr_chat_room = ChatRoom.objects.get(chat_room_id=chat_room_id)
        user_id = curr_chat_room.user_id
        topic = curr_chat_room.topic

        queryset = Feedback.objects.filter(user=user_id, topic=topic)
        serializer = feedbackSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)