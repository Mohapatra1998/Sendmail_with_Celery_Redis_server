from celery import shared_task
from time import sleep
from django.core.mail import send_mail
@shared_task
def sleepy(duarition):
    sleep(duarition)
    return None
@shared_task
def send_mail_task():
    send_mail('CELERY WORKED OK', 'CELERY IS HOT', 'mohapatrasandip199@gmail.com', ['sandip@assentglobal.us'], fail_silently=False)