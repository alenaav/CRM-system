from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from .decorators import login_required, admin_required


# ЛОГИН
def login_view(request):
    error = ''

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        try:
            user = Employee.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            return redirect('главная')
        except:
            error = 'Неверный логин или пароль'

    return render(request, 'login.html', {'error': error})


# ВЫХОД
def logout_view(request):
    request.session.flush()
    return redirect('login')


# СПИСОК СОТРУДНИКОВ (доступен всем авторизованным)
@login_required
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees_list.html', {'employees': employees})


# СОЗДАНИЕ (только админ)
@admin_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('сотрудники')
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})


# РЕДАКТИРОВАНИЕ (только админ)
@admin_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('сотрудники')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee_form.html', {'form': form})


# УДАЛЕНИЕ (только админ)
@admin_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('сотрудники')