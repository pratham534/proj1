from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    students = Student.objects.all()
    return JsonResponse({'students': list(students.values())})