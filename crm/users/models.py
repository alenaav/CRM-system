from django.db import models

class Employee(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('employee', 'Сотрудник'),
    )

    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES)

    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=100)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name