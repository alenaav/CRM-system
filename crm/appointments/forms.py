from django import forms
from .models import Appointment, Schedule

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'employee', 'service', 'date', 'time', 'status']
        labels = {
            'client': 'Клиент',
            'employee': 'Сотрудник',
            'service': 'Услуга',
            'date': 'Дата',
            'time': 'Время',
            'status': 'Статус',
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'date', 'start_time', 'end_time']
        labels = {
            'employee': 'Сотрудник',
            'date': 'Дата',
            'start_time': 'Начало',
            'end_time': 'Конец',
        }