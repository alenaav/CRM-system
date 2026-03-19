from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='услуги'),
    path('создать/', views.service_create, name='создать_услугу'),
    path('<int:pk>/редактировать/', views.service_edit, name='редактировать_услугу'),
    path('<int:pk>/удалить/', views.service_delete, name='удалить_услугу'),
]