from django.shortcuts import render
from .models import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTPRecipientsRefused
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



def index(request):
  template = 'index.html'
  context = {
  'title': "GUARDIAN",
  }
  return render(request, template, context)


def mail(request):
  template = 'mail.html'
  context = {
  'title': "GUARDIAN",
  }
  return render(request, template, context)


def sendmail(request):

  deliveries = Trailer.objects.all().order_by('-id')

  new_context = {
  'trailer': deliveries.trailer,
  'cons': deliveries,
  }
  template = get_template('mail.html')
  html_content = template.render(new_context)


  fromaddr = "itzli2000@gmail.com"
  toaddr = email_user
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Información de ventas 'ICE'"
  body = html_content
  msg.attach(MIMEText(body, 'html'))
  # msg.attach('invoice.csv', csvfile.getvalue(), 'text/csv')
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(fromaddr, "molinona&9")
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

  return render(request, template, context)