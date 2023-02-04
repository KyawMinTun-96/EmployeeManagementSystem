from django.shortcuts import render
#from employee.models import Department, Position, Employees



# from django.shortcuts import redirect, render
from django.http import HttpResponse
# from employee_information.models import Department, Position, Employees
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# import json


# Create your views here.
def home(request):
    context = {
        'page_title':'Home',
    }
    return render(request, 'ems_info/home.html', context)


def departments(request):
    context = {
        'page_title':'Department',
    }
    return render(request, 'ems_info/departments.html', context)


def projects(request):
    context = {
        'page_title' : 'Project',
    }
    return render(request, 'ems_info/projects.html', context)


def positions(request):
    context = {
        'page_title' : 'Position',
    }
    return render(request, 'ems_info/positions.html', context)


def employees(request):
    context = {
        'page_title' : 'Employee',
    }
    return render(request, 'ems_info/employees.html', context)