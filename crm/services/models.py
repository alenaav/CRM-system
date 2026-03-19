from django.db import models

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name