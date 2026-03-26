from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.views.decorators.http import require_http_methods
import calendar
from datetime import date
from django.utils.safestring import mark_safe
from django.db.models import Prefetch
from .models import Appointment
from users.decorators import login_required

# Записи

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

class ScheduleCalendar(calendar.HTMLCalendar):
    def __init__(self, year, month, appointments):
        super().__init__(firstweekday=0)  # 0 = Monday
        self.year = year
        self.month = month
        # appointments сгруппируем по дате
        self.appointments_by_day = {}
        for a in appointments:
            self.appointments_by_day.setdefault(a.date.day, []).append(a)

    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        aps = self.appointments_by_day.get(day, [])
        items = ''
        for a in aps:
            items += f'<div class="small">{a.time.strftime("%H:%M")} {a.employee.name} – {a.service.name}</div>'

        return f'<td class="day"><span class="date">{day}</span>{items}</td>'

    def formatmonth(self, withyear=True):
        html = super().formatmonth(self.year, self.month, withyear=withyear)
        return html.replace(
            '<table border="0" cellpadding="0" cellspacing="0"',
            '<table class="calendar"'
        )


@login_required
def schedule_calendar(request, year=None, month=None):
    today = date.today()
    year = int(year or today.year)
    month = int(month or today.month)

    # подтянем связанные сущности
    appointments = (
        Appointment.objects
        .filter(date__year=year, date__month=month)
        .select_related('employee', 'service')
    )

    cal = ScheduleCalendar(year, month, appointments)
    html_cal = cal.formatmonth(withyear=True)

    # посчитаем соседние месяца для навигации
    prev_month = month - 1 or 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    context = {
        'calendar': mark_safe(html_cal),
        'year': year,
        'month': month,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }
    return render(request, 'schedule_calendar.html', context)