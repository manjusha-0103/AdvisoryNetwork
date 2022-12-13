# Create your models here.
from django.db import models
from django.utils import timezone

class Advisor_info(models.Model):
    name = models.CharField(max_length=200, default="")
    photo = models.ImageField(upload_to='advisor_img/')
    note_time = models.DateTimeField('note time', default=timezone.now)

    @property
    def __str__(self):
        return f"self.name"