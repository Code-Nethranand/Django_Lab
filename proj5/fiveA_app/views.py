from django.shortcuts import render,HttpResponse
from .models import Student,Course

def index(request):
    courses=Course.objects.values_list('name',flat=True).distinct()
    obj = Student.objects.all()
    return render(request,'form.html',{'obj':obj,'courses':courses})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        course = request.POST['course']
        usn = request.POST['usn']
        sec = request.POST['sec']
        obj = Student(name=name,email=email,dob=dob,gender=gender,course=course,sec=sec,usn=usn)
        obj.save()
        success='Registration Completed for ' + name
        return HttpResponse(success)
     