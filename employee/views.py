from django.shortcuts import render
from employee.models import Department, Position, Employee
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json

def home(request):
    context = {
        'page_title':'Home',
        'total_department':len(Department.objects.filter(status=1).all()),
        'total_position' : len(Position.objects.filter(status=1).all()),
        'total_employee' : len(Employee.objects.filter(status=1).all())
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

def employees(request):
    employee_list = Employee.objects.all()
    context = {
        'page_title' : 'Employee',
        'employees' : employee_list,
    }
    return render(request, 'ems_info/employees.html', context)




def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title' : 'Position',
        'positions'  : position_list,
    }
    return render(request, 'ems_info/positions.html', context)

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
        'department' : department
    }
    return render(request, 'ems_info/add_department.html', context)

def add_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'ems_info/add_position.html', context)


def add_employees(request):
    employee = {}
    departments = Department.objects.filter(status=1).all()
    positions = Position.objects.filter(status = 1).all()

    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employee.objects.filter(id=id).first()
            
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions,

    }
    return render(request, 'ems_info/add_employee.html', context)

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


def save_positions(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        if(data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'],
            description = data['description'], status = data['status'])

        else:
            save_position = Position(name=data['name'], description = data['description'], status=data['status'])
            save_position.save()
        resp['status'] = 'success'

    except:
        resp['statua'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")





def save_employees(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employee.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employee.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employee.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,hired_date = data['hired_date'],salary = data['salary'],status = data['status'])
            else:
                save_employee = Employee(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,hired_date = data['hired_date'],salary = data['salary'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"hired_date" : data['hired_date'],"salary" : data['salary'],"status" : data['status']}))
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



def delete_positions(request):
    data = request.POST
    resp = {'status' : 'failed'}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['statu'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def delete_employees(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employee.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")



def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status=1).all()
    positions = Position.objects.filter(status=1).all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']

        if id.isnumeric() and int(id) > 0:
            employee = Employee.objects.filter(id=id).first()

    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }

    return render(request, 'ems_info/view_employee.html', context)