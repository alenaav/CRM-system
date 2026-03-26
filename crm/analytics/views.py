from django.shortcuts import render
from django.db.models import Count, Sum
from appointments.models import Appointment
from users.models import Employee
from services.models import Service
from datetime import timedelta
from django.utils import timezone


def analytics_dashboard(request):
    today = timezone.now().date()
    
    # Фильтры
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    employee_id = request.GET.get('employee')
    service_id = request.GET.get('service')
    
    qs = Appointment.objects.select_related('client', 'employee', 'service')
    
    if date_from:
        qs = qs.filter(date__gte=date_from)
    if date_to:
        qs = qs.filter(date__lte=date_to)
    if employee_id:
        qs = qs.filter(employee_id=employee_id)
    if service_id:
        qs = qs.filter(service_id=service_id)
    
    # Метрики
    total_appointments = qs.count()
    total_revenue = qs.aggregate(total=Sum('service__price'))['total'] or 0
    
    # Статистика
    employee_stats = (
        qs.values('employee__name')
        .annotate(count=Count('id'), revenue=Sum('service__price'))
        .order_by('-count')
    )
    
    service_stats = (
        qs.values('service__name')
        .annotate(count=Count('id'), revenue=Sum('service__price'))
        .order_by('-revenue')
    )
    
    top_clients = (
        qs.values('client__name')
        .annotate(count=Count('id'))
        .order_by('-count')[:3]
    )
    
    context = {
        'total_appointments': total_appointments,
        'total_revenue': total_revenue,
        'employee_stats': employee_stats,
        'service_stats': service_stats,
        'top_clients': top_clients,
        'date_from': date_from,
        'date_to': date_to,
        'employees': Employee.objects.all(),
        'services': Service.objects.all(),
    }
    return render(request, 'analytics.html', context)