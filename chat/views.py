from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from .talkgenerater import *


class ChatView(APIView):
    def get(self, request, topic, user_id):
        # 입력받은 정보 바탕으로 채팅방 생성
        input_data = {'topic': topic, 'user': user_id}
        chat_room = chatRoomSerializer(data=input_data)
        if chat_room.is_valid():
            chat_room.save()
            chat_room_id = chat_room.data['chat_room_id']

            #토픽에 관련된 문장 5개 생성
            questions = TalkGenerator.start(self, topic)
            for q in questions:
                msg = {"chat_room": chat_room_id, "is_answer": False, "is_send": False, "message": q}
                new_chat = messageSerializer(data=msg)
                if new_chat.is_valid():
                    new_chat.save()
                else:
                    return Response(new_chat.errors, status=status.HTTP_400_BAD_REQUEST)
            q1 = Chat.objects.get(message=questions[0])
            q1.is_send = True
            q1.save()
            output_json = {"chat_room_id": chat_room_id, "question": questions[0]}
            return Response(output_json, status=status.HTTP_200_OK)
        return Response(chat_room.errors, status=status.HTTP_400_BAD_REQUEST)





