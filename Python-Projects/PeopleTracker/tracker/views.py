from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
 	student_list = Student.objects.all().order_by("last_name")
	return render(request, 'tracker/index.html', {"student_list": student_list})

def detail(request, last_name, first_name):
	s = Student.objects.get(last_name=last_name, first_name=first_name)
	students_in = {
		"per_1": Student.objects.filter(class_per1=s.class_per1),
		"per_2": Student.objects.filter(class_per2=s.class_per2),
		"per_3": Student.objects.filter(class_per3=s.class_per3),
		"per_4": Student.objects.filter(class_per4=s.class_per4),
		"per_5": Student.objects.filter(class_per5=s.class_per5),
		"per_6": Student.objects.filter(class_per6=s.class_per6),
		"per_7": Student.objects.filter(class_per7=s.class_per7),
		"per_8": Student.objects.filter(class_per8=s.class_per8),
	}
	return render(request, 'tracker/detail.html', {"student": s,"students_in": students_in})
