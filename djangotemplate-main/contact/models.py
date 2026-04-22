from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    message = models.TextField(max_length=250)
