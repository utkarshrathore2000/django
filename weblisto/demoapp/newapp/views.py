from django.shortcuts import render,redirect
from django.http import HttpResponse
from newapp.forms import employeform
from newapp.models import Employee
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def form(request):
    if request.method=='POST':
        obj=employeform(request.POST)
        if obj.is_valid():
            obj.save()
            return render(request,'show.html')
    else:
     #   import pdb; pdb.set_trace()
        obj=employeform()
        return render(request,'form.html',{'obj':obj})
def show(request):
    obj=Employee.objects.all()
    return render(request,'show.html',{'obj':obj})
