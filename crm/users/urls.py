from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees_list, name='сотрудники'),
    path('создать/', views.employee_create, name='создать_сотрудника'),
    path('<int:pk>/редактировать/', views.employee_edit, name='редактировать_сотрудника'),
    path('<int:pk>/удалить/', views.employee_delete, name='удалить_сотрудника'),
]