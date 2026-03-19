from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'duration', 'price']
        labels = {
            'name': 'Название',
            'duration': 'Длительность (мин)',
            'price': 'Цена',
        }