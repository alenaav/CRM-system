from django.urls import path
from . import views

urlpatterns = [
    # Записи
    path('', views.appointments_list, name='записи'),
    path('создать/', views.appointment_create, name='создать_запись'),
    path('<int:pk>/редактировать/', views.appointment_edit, name='редактировать_запись'),
    path('<int:pk>/удалить/', views.appointment_delete_confirm, name='удалить_запись'),

    # Календарь
    path('календарь/', views.schedule_calendar, name='календарь'),
    path('календарь/<int:year>/<int:month>/', views.schedule_calendar, name='календарь_месяц'),
]