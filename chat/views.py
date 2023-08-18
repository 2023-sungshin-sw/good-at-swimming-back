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


# 1. 입력 받은 대답 채팅에 저장
# 2. 입력 받은 대답을 평가해 피드백에 저장
# 3. 전체 대화 리스트를 전달
# 4. 프론트에서 next == false일 경우, 전체 대화 리스트 크기가 10이면 끝나면 채팅 입력칸 막아주기
class ChatListView(APIView):
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
        feedback_json = {"user": user_id, "topic": topic, "original_sentence": input_json["message"], "fix_sentence": feedback_msg}
        new_feedback = feedbackSerializer(data=feedback_json)
        if new_feedback.is_valid():
            new_feedback.save()
        else:
            return Response(new_feedback.errors, status=status.HTTP_400_BAD_REQUEST)

        # 3. 전체 대화 리스트를 전달
        next_question = Chat.objects.filter(chat_room=input_json["chat_room"], is_answer=False, is_send=False).first()
        next_question.is_send = True
        next_question.save()
        queryset = Chat.objects.filter(chat_room=input_json["chat_room"], is_send=True)
        serializer = messageSerializer(queryset, many=True)
        chats = serializer.data
        output_json = {"next": True, "data": chats}
        if len(chats) == 10:
            output_json["next"] = False
            output_json["next"] = False
        return Response(output_json, status=status.HTTP_201_CREATED)








