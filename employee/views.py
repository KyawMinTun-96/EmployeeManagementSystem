from django.shortcuts import render
#from employee.models import Department, Position, Employees



# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from employee_information.models import Department, Position, Employees
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect
# import json


# Create your views here.
def home(request):
    context = {
        'page_title':'Home',
    #     # 'employees':employees,
    #     'total_department':len(Department.objects.all()),
    #     'total_position':len(Position.objects.all()),
    #     'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'ems_info/home.html', context)