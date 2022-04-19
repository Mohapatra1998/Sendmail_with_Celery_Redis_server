from django.shortcuts import render, HttpResponse
from . task import *
from django.core.mail import send_mail
# Create your views here.
# def send_mail_without_celery():
#     send_mail('CELERY WORKED OK', 'CELERY IS HOT', 'mohapatrasandip199@gmail.com', ['sandip@assentglobal.us'], fail_silently=False)
def index(request):
    # sleepy.delay(10)
    # send_mail_without_celery()
    send_mail_task.delay()
    return HttpResponse('<h2>Hello celery page<h2>')