from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services_list.html', {'services': services})

def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('услуги')
    else:
        form = ServiceForm()
    return render(request, 'service_form.html', {'form': form})

def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('услуги')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('услуги')