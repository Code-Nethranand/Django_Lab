from django.shortcuts import render
from fiveA_app.models import Student
import json
from django.http import JsonResponse
def search(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        students=Student.objects.filter(name__startswith=search_str) | Student.objects.filter(usn__startswith=search_str) | Student.objects.filter(course__startswith=search_str)
        data = students.values()
        return JsonResponse(list(data), safe=False)

def stlist(request):
    obj = Student.objects.all()
    return render(request, "stlist.html", {'obj': obj})