from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from mailing_create.create_mail import new_mailing

from clients_and_notes.models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Message

class MailingSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'start_time', 'text', 'filter', 'finish_time', 'messages')
        model = Mailing


