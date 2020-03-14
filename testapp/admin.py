from django.contrib import admin
from .models import Reqdata,Reqtype,Status,State

# Register your models here.

admin.site.register(Reqdata)
admin.site.register(Reqtype)
admin.site.register(Status)
admin.site.register(State)