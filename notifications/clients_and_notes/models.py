from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Mailing(models.Model):
    start_time = models.DateTimeField(auto_now_add=False, blank=False)
    text = models.TextField()
    filter = models.CharField(max_length=100)
    finish_time = models.DateTimeField(auto_now_add=False, blank=False)

class Client(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    phone_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=30)
    timezone = models.CharField(max_length=10)

class Message(models.Model):
    send_time = models.DateTimeField(auto_now_add=False, blank=False)
    send = models.BooleanField()
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE,
        blank=True, null=True
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        blank=True, null=True
    )
