from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import PeriodicTask
from clients_and_notes.models import Client
import datetime
from django.utils import timezone

MAILING_ID = 'ok'
MESSAGE = 'ok'
CLIENTS_PHONE_NUMBERS = []


def mailing_creation(mailing_id, start_time):
    clocked_task = ClockedSchedule.objects.create(clocked_time=start_time)
    task = PeriodicTask.objects.create(
        clocked=clocked_task, name=f'task.{mailing_id}',
        task='mailing_create.tasks.send_message',
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
    mailing_creation(mailing_id, start_time)
    global MAILING_ID
    MAILING_ID = mailing_id
    global MESSAGE
    MESSAGE = message
    global CLIENTS_PHONE_NUMBERS
    CLIENTS_PHONE_NUMBERS = clients_phone_numbers
