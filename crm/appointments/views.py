from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment, Schedule
from .forms import AppointmentForm, ScheduleForm
from django.views.decorators.http import require_http_methods

# Записи
def appointments_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments_list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('записи')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('записи')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

@require_http_methods(["GET", "POST"])
def appointment_delete_confirm(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        if "confirm" in request.POST:
            appointment.delete()
        return redirect('записи')
    return render(request, 'appointment_delete_confirm.html', {'appointment': appointment})

def appointments_list(request):
    search = request.GET.get('q', '').strip()
    appointments = Appointment.objects.select_related('client', 'employee', 'service')
    if search:
        appointments = appointments.filter(client__name__icontains=search)
    return render(request, 'appointments_list.html', {
        'appointments': appointments,
        'search': search,
    })

# Расписание
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def schedule_create(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('расписание')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_form.html', {'form': form})

def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('расписание')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedule_form.html', {'form': form})

def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    schedule.delete()
    return redirect('расписание')