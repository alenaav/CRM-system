from django.db import models
from clients.models import Client
from users.models import Employee
from services.models import Service

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Запланировано'),
        ('completed', 'Выполнено'),
        ('canceled', 'Отменено'),
    )

    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Schedule(models.Model):
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    start_time = models.TimeField('Начало')
    end_time = models.TimeField('Конец')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'