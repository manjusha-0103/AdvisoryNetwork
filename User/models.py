from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.forms import UserCreationForm

class Register(models.Model):
    form = UserCreationForm()
    username = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="", null=True)
    note_time = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return (f'{self.name} {self.email} {self.password}')


class Userlogin(models.Model):
    email = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="", null=True)
    note_time = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return (f'{self.email} {self.password}')

class Bookcall(models.Model):
    pass
