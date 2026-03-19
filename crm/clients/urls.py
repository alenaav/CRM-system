from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='клиенты'),
    path('создать/', views.client_create, name='создать_клиента'),
    path('<int:pk>/редактировать/', views.client_edit, name='редактировать_клиента'),
    path('<int:pk>/удалить/', views.client_delete, name='удалить_клиента'),
]