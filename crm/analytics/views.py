from django.shortcuts import render
from appointments.models import Appointment
from users.models import Employee
from services.models import Service

def analytics_view(request):
    total = Appointment.objects.count()

    employee_stats = {
        e.name: Appointment.objects.filter(employee=e).count()
        for e in Employee.objects.all()
    }

    service_stats = {
        s.name: Appointment.objects.filter(service=s).count()
        for s in Service.objects.all()
    }

    return render(request, 'analytics.html', {
        'total_appointments': total,
        'employee_load': employee_stats,
        'service_stats': service_stats
    })