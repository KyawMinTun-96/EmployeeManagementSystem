from django.shortcuts import render
from employee.models import Department
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json



def home(request):
    context = {
        'page_title':'Home',
    }
    return render(request, 'ems_info/home.html', context)


def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Department',
        'departments':department_list,
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



def add_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()

    context = {
        'page_title' : department
    }
    return render(request, 'ems_info/add_department.html', context)



def save_departments(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        if(data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'],
            description = data['description'], status = data['status'])

        else:
            save_department = Department(name=data['name'], description = data['description'], status=data['status'])
            save_department.save()
        resp['status'] = 'success'

    except:
        resp['statua'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



def delete_departments(request):
    data =  request.POST
    resp = {'status' : 'failed'}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


