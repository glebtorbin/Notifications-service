from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from mailing_create.create_mail import new_mailing
from clients_and_notes.models import Client, Mailing, Message
from .serializers import (
    ClientSerializer, MailingSerializer,
    MessageSerializer
)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def create(self, request):
        post = Mailing.objects.all()
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_mailing(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer