from django.shortcuts import render
from .models import Student,Course

def home(request):
    return render(request,'home.html')

def stlist(request):
    courses = Student.objects.values_list('course', flat=True).distinct()
    obj = Student.objects.all()
    return render(request, "stlist.html", {'obj': obj})

def colist(request):
    obj = Course.objects.all()
    return render(request, "colist.html", {'obj': obj})