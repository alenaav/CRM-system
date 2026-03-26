from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics_dashboard, name='аналитика'),
    path('нагрузка_по_дням/', views.employee_daily_stats, name='нагрузка_по_дням'),
]