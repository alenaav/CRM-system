from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services'),
    path('create/', views.service_create, name='service_create'),
    path('update/<int:pk>/', views.service_update, name='service_update'),
    path('delete/<int:pk>/', views.service_delete, name='service_delete'),
]