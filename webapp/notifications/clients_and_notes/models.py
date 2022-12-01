from django.db import models

class Mailing(models.Model):
    start_time = models.DateTimeField(auto_now_add=False, blank=False)
    text = models.TextField()
    filter = models.CharField(max_length=100)
    finish_time = models.DateTimeField(auto_now_add=False, blank=False)


class Client(models.Model):
    phone = models.IntegerField(null=False, blank=False, unique=True)
    phone_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=30)
    timezone = models.CharField(max_length=10)


class Message(models.Model):
    send_time = models.DateTimeField(auto_now_add=False, blank=False)
    send_status = models.BooleanField(default=True)
    mailing = models.ForeignKey(
        Mailing, related_name='messages',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        blank=True, null=True
    )
