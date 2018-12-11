import json

import requests
from django.shortcuts import render

from .models import Contact
import smtplib
from email.message import EmailMessage


def index(request):
    return render(request, 'mysite/index1.html', dict())


def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        subject = request.POST.get('Subject')
        _replyto = request.POST.get('_replyto')

        c = Contact(email=_replyto, subject=subject, message=message)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/index1.html')
