from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']
        labels = {
            'name': 'Название услуги',
            'price': 'Цена',
        }