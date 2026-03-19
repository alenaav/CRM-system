from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients'),
    path('create/', views.client_create, name='client_create'),
    path('update/<int:pk>/', views.client_update, name='client_update'),
    path('delete/<int:pk>/', views.client_delete, name='client_delete'),
]