from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from clients_and_notes.models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Mailing


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Message