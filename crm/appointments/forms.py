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
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
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
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }