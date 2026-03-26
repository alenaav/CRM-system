from django import forms
from .models import Appointment

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