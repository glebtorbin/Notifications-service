from http import HTTPStatus
import os
import json
from notifications.celery import shared_task
import requests
from datetime import datetime
from django.utils import timezone

from mailing_create.create_mail import MAILING_ID, MESSAGE, CLIENTS_PHONE_NUMBERS
from clients_and_notes.models import Client, Mailing, Message
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv('TOKEN')
SEND_API_ENDPOINT = 'https://probe.fbrq.cloud/v1/send/'

@shared_task
def send_message():
    for phone_number in CLIENTS_PHONE_NUMBERS:
        client = Client.objects.get(phone=phone_number)
        new_message = Message.objects.create(
            send_time = datetime.now(),
            send_status = False,
            mailing = Mailing.objects.get(id=MAILING_ID),
            client = client
        )
        data = {
            "id": new_message.id,
            "phone": phone_number,
            "text": MESSAGE
        }
        headers = {
            'Authorization': TOKEN
        }
        response = requests.post(SEND_API_ENDPOINT+f'{new_message.id}', headers=headers, data=json.dumps(data))
        if response.status_code == HTTPStatus.OK:
            new_message.send_status = True
        print(response.status_code)
