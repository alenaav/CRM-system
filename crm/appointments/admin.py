from django.contrib import admin
from .models import Appointment, Schedule

admin.site.register(Appointment)
admin.site.register(Schedule)