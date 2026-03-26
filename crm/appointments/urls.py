from django.urls import path
from . import views

urlpatterns = [
    # Записи
    path('', views.appointments_list, name='записи'),
    path('создать/', views.appointment_create, name='создать_запись'),
    path('<int:pk>/редактировать/', views.appointment_edit, name='редактировать_запись'),
    path('<int:pk>/удалить/', views.appointment_delete_confirm, name='удалить_запись'),

    # Расписание
    path('расписание/', views.schedule_list, name='расписание'),
    path('расписание/создать/', views.schedule_create, name='создать_расписание'),
    path('расписание/<int:pk>/редактировать/', views.schedule_edit, name='редактировать_расписание'),
    path('расписание/<int:pk>/удалить/', views.schedule_delete, name='удалить_расписание'),
    path('календарь/', views.schedule_calendar, name='календарь'),
    path('календарь/<int:year>/<int:month>/', views.schedule_calendar, name='календарь_месяц'),
]