from django.shortcuts import render,redirect
from employee.forms import EmployeeForm
from employee.models import Employee
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = EmployeeForm()
        return render(request,'index.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return 

