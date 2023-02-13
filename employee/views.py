from django.shortcuts import render
from employee.models import Department, Position, Employee, Project
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json

@login_required
def home(request):
    context = {
        'page_title':'Home',
        'total_department':len(Department.objects.filter(status=1).all()),
        'total_position' : len(Position.objects.filter(status=1).all()),
        'total_employee' : len(Employee.objects.filter(status=1).all()),
        'total_project' : len(Project.objects.filter(status=1).all())
    }
    return render(request, 'ems_info/home.html', context)

def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')


def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Department',
        'departments':department_list,
    }
    return render(request, 'ems_info/departments.html', context)

@login_required
def projects(request):
    project_list = Project.objects.all()
    context = {
        'page_title' : 'Project',
        'projects' : project_list,
    }
    return render(request, 'ems_info/projects.html', context)

@login_required
def employees(request):
    employee_list = Employee.objects.all()
    context = {
        'page_title' : 'Employee',
        'employees' : employee_list,
    }
    return render(request, 'ems_info/employees.html', context)
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title' : 'Position',
        'positions'  : position_list,
    }
    return render(request, 'ems_info/positions.html', context)

@login_required
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


@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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
            # print(Exception)
            # print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"hired_date" : data['hired_date'],"salary" : data['salary'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_departments(request):
    data =  request.POST
    resp = {'status' : 'failed'}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_positions(request):
    data = request.POST
    resp = {'status' : 'failed'}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['statu'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employees(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employee.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
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

@login_required
def add_projects(request):

    project = {}
    departments = Department.objects.filter(status=1).all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            project = Project.objects.filter(id=id).first()

    context = {
        'project' : project,
        'departments' : departments
    }

    return render(request, 'ems_info/add_project.html', context )

@login_required
def save_projects(request):
    data = request.POST
    resp = {'status': 'failed'}

    try:
        dept = Department.objects.filter(id=data['department_id']).first()
        if(data['id']).isnumeric() and int(data['id']) > 0 :
            save_project = Project.objects.filter(id = data['id']).update(name=data['name'],
            department_id = dept, start_date = data['start_date'], end_date= data['end_date'], status = data['status'])

        else:
            save_project = Project(name=data['name'], department_id = dept, 
            start_date = data['start_date'], end_date= data['end_date'], status = data['status'])
            save_project.save()

        resp['status'] = 'success'

    except Exception:
        resp['statua'] = 'failed'
        # print(Exception)
        # print(json.dumps({'name':data['name'], 'department_id': data['department_id'], 'start_date': data['start_date'], 'end_date': data['end_date'], 'status': data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_projects(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Project.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type='application/json');

@login_required
def view_project(request):

    project = {}
    departments = Department.objects.filter(status=1).all()

    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']

        if id.isnumeric() and int(id) > 0:
            project = Project.objects.filter(id=id).first()

    context = {
        'project' : project,
        'departments' : departments,
    }
    return render(request, 'ems_info/view_projects.html', context)