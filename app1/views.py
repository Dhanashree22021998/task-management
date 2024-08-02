from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def addview(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/v1/s1/")
    return render(request,"app1/add.html",{"form":form})

def showview(request):
    obj = Employee.objects.all()
    return render(request,"app1/show.html",{"employee":obj})

def updateview(request,id):
    obj = Employee.objects.get(eid=id)
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/v1/s1/')
    return render(request,"app1/add.html",{"form":form})

def deleteview(request,id):
    obj = Employee.objects.get(eid = id)
    if request.method =="POST":
        obj.delete()
        return redirect("/v1/s1/")
    return render(request,"app1/confirm.html",{"obj":obj})