from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone', 'role', 'login', 'password']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'role': 'Роль',
            'login': 'Логин',
            'password': 'Пароль',
        }
        widgets = {
            'password': forms.PasswordInput()
        }