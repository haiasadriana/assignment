from rest_framework import serializers
from .models import Chat
from .models import Conversation
from .models import Schedule


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['chatId', 'payload', 'userId', 'utc_date', 'status']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['payload', 'userId']


class ConversationSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['conversationId', 'storeId', 'operatorId', 'clientId', 'operatorGroup', 'chat']
