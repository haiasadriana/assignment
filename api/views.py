from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChatSerializer
from .serializers import ConversationSerializer
from .serializers import ScheduleSerializer
from .models import Chat
from .models import Conversation
from .models import Schedule


class ChatList(APIView):
    def get(self, request):
        queryset = Chat.objects.all()
        serializer_class = ChatSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = ScheduleSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
