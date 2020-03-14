from django.db import models
from datetime import datetime
import uuid
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from Testpro.utils import unique_slug_generator

# Create your models here.


class Reqtype(models.Model):
    typ = models.CharField(max_length=30)
    
    def __str__(self):
        return "{}".format(self.typ)
    


class State(models.Model):
    stat = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.stat)


class Status(models.Model):
    statuss = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.statuss)


class Reqdata(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length = 250, unique=True, null=True, blank=True)
    Requesttype = models.ManyToManyField(Reqtype)
    Reqdisc = models.CharField(max_length=20)
    date_modified = models.DateTimeField(default=datetime.now())
    city = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    Altermob = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    remarks = models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.Reqdisc)


# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
        
# post_save.connect(slug_generator, sender=Reqdata)

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.IntegerField()