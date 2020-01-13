from django.shortcuts import render,redirect
from django.http import HttpResponse
from ourapp.forms import employeform
from ourapp.models import details
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
            try:
                obj.save()
                return redirect('')
            except:
                pass
    else:
        obj=employeform()
        return render(request,'form.html',{'obj':obj})
