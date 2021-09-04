from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=1000)
    message_title = models.CharField(max_length=100)
    message_sender = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date sended")