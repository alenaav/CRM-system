from django.shortcuts import render
from appointments.models import Appointment
from users.models import Employee
from services.models import Service
from django.db.models import Count
from django.db.models.functions import TruncDate

def analytics_dashboard(request):
    total_appointments = Appointment.objects.count()

    # Сколько записей у каждого сотрудника
    employee_load = Appointment.objects.values('employee__name').annotate(count=Count('id'))
    employee_stats = {e['employee__name']: e['count'] for e in employee_load}

    # Сколько записей по каждой услуге
    service_load = Appointment.objects.values('service__name').annotate(count=Count('id'))
    service_stats = {s['service__name']: s['count'] for s in service_load}

    context = {
        'total_appointments': total_appointments,
        'employee_load': employee_stats,
        'service_stats': service_stats
    }

    return render(request, 'analytics.html', context)

def employee_daily_stats(request):
    stats = (
        Appointment.objects
        .annotate(day=TruncDate('date'))
        .values('employee__name', 'day')
        .annotate(count=Count('id'))
        .order_by('employee__name', 'day')
    )
    return render(request, 'employee_daily_stats.html', {'stats': stats})