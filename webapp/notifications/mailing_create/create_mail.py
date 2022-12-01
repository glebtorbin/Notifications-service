from clients_and_notes.models import Client
from .tasks import send_message

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
    send_message(mailing_id, message, clients_phone_numbers)
    return start_time, message, clients_phone_numbers, end_time


