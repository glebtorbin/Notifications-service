# Generated by Django 3.2.16 on 2022-11-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_and_notes', '0002_rename_send_message_send_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_status',
            field=models.BooleanField(default=True),
        ),
    ]