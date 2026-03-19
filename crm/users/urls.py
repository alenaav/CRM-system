from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees_list, name='employees'),
    path('create/', views.employee_create, name='employee_create'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]