from django.db import models
from django.core.validators import RegexValidator


class Conversation(models.Model):
    conversationId = models.IntegerField(null=False, primary_key=True)
    storeId = models.IntegerField(null=False)
    operatorId = models.IntegerField(null=False)
    clientId = models.IntegerField(null=False)
    operatorGroup = models.CharField(max_length=32)


class Chat(models.Model):
    class Status(models.TextChoices):
        NEW = 'new'
        SENT = 'sent'

    chatId = models.IntegerField(null=True, blank=True)
    payload = models.TextField(max_length=300,
                               validators=[RegexValidator("[a-zA-Z]+\d+\W+\_\-\\\/\~\@\#\$\%\^\&\*\(\)\!\?")])
    userId = models.IntegerField(null=False)
    utc_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    conversation = models.ForeignKey(Conversation, null=True, on_delete=models.CASCADE, related_name='chat')

    class Meta:
        ordering = ['chatId']


class Schedule(models.Model):
    class Status(models.TextChoices):
        NEW = 'new'
        SENT = 'sent'

    chatId = models.IntegerField(null=True, blank=True)
    payload = models.TextField(max_length=300,
                               validators=[RegexValidator("[a-zA-Z]+\d+\W+\_\-\\\/\~\@\#\$\%\^\&\*\(\)\!\?")])
    userId = models.IntegerField(null=False)
    utc_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default='new')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='schedule')
