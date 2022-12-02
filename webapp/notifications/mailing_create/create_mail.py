from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import PeriodicTask
from clients_and_notes.models import Client
from .tasks import send_message
import datetime
from django.utils import timezone

def mailing_creation(mailing_id, start_time, message, clients_phone_numbers, end_time):
    clocked_task = ClockedSchedule.objects.create(clocked_time=timezone.now())
    task = PeriodicTask.objects.create(
        clocked=clocked_task, name=f'task.{mailing_id}',
        task=f'mailing_create.tasks.send_message({mailing_id}, {message}, {clients_phone_numbers})',
        one_off=True
    )
    

def new_mailing(data):
    start_time = data['start_time']
    message = data['text']
    filter = data['filter']
    mailing_id = data['id']
    clients_phone_numbers = []
    for client in Client.objects.all():
        if filter == client.tag or filter == client.phone_code:
            clients_phone_numbers.append(client.phone)
    end_time = data['finish_time']
    print(clients_phone_numbers)
    mailing_creation(mailing_id, start_time, message, clients_phone_numbers, end_time)
