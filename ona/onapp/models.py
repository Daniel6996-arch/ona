from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class StartDate(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    
class OnaData(models.Model):
    name = models.CharField(max_length = 120, blank=True, null=True)
    age =models.IntegerField(blank=True, null=True)
    gender =models.TextField(blank=True, null=True)
    employment =models.TextField(blank=True, null=True)
    status =models.TextField(blank=True, null=True)
    image_url =models.CharField(max_length=120, blank=True, null=True)
    
    def _str_(self):
        return self.name