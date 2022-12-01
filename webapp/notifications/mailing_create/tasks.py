import os
import json
from celery import shared_task
import requests
from datetime import datetime

from clients_and_notes.models import Client, Mailing, Message
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv('TOKEN')
SEND_API_ENDPOINT = 'https://probe.fbrq.cloud/v1/send/'

# @shared_task
def send_message(mailing_id, text, phone_numbers):
    for phone_number in phone_numbers:
        client = Client.objects.get(phone=phone_number)
        new_message = Message.objects.create(
            send_time = datetime.now(),
            send_status = True,
            mailing = Mailing.objects.get(id=mailing_id),
            client = client
        )
        data = {
            "id": new_message.id,
            "phone": phone_number,
            "text": text
        }
        headers = {
            'Authorization': TOKEN
        }
        response = requests.post(SEND_API_ENDPOINT+f'{new_message.id}', headers=headers, data=json.dumps(data))
        print(response.status_code)
