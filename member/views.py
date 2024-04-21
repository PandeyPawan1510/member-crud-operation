from django.shortcuts import render,redirect
from .forms import Empforms
from . models import Student
# Create your views here.
def home(request):
    thakur=Student.objects.all()
    return render(request,"home.html",{'thakur':thakur})

def addstu(request):
    if request.method=="POST":
       print("chetan")
       thakur_roll=request.POST.get("std_roll")
       thakur_name=request.POST.get("std_name")
       thakur_email=request.POST.get("std_email")
       thakur_address=request.POST.get("std_address")
       thakur_phone=request.POST.get("std_phone")

       s=Student()
       s.roll=thakur_roll
       s.name=thakur_name
       s.email=thakur_email
       s.address=thakur_address
       s.phone=thakur_phone
       s.save()
       return redirect("/")
 
    return render(request,"add.html")

def delete_thakur(request, roll):
    s = Student.objects.get(pk=roll)

    s.delete()
    return redirect("/")

def update_thakur(request,roll):
    obj =  Student.objects.get(id=roll)
    if request.method == "POST":
        data = Empforms(request.POST,instance=obj)
        data.save()
        return redirect("/details")
    else:
        d={
            "form":Empforms(instance=obj)
        }

        return render(request,"add.html",d)
    

def del3(request):
    obj =Student.objects.all()
    obj.delete()
    return redirect("/")