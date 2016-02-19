from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import *

def students(request):
	student_list = Student.objects.all().order_by("last_name")
	return render(request, 'tracker/index.html', {"student_list": student_list})
	
def index(request):
	search = False
	error = None
	student_list = []
	post = None

 	if request.method == "POST":
 		search = True
 		post = request.POST["last_name"]
 		student_list = Student.objects.all().filter(last_name__icontains=post)
	 	if not post or not student_list:
	 		error = "No results."
	 		search = False
	 		student_list = None
	return render(request, 'tracker/who.html', {"student_list": student_list, "search":search, "error": error})

def detail(request, last_name, first_name):
	s = Student.objects.get(last_name=last_name, first_name=first_name)
	students_in = {
		"per_1": Student.objects.filter(class_per1=s.class_per1).exclude(first_name=first_name, last_name=last_name),
		"per_2": Student.objects.filter(class_per2=s.class_per2).exclude(first_name=first_name, last_name=last_name),
		"per_3": Student.objects.filter(class_per3=s.class_per3).exclude(first_name=first_name, last_name=last_name),
		"per_4": Student.objects.filter(class_per4=s.class_per4).exclude(first_name=first_name, last_name=last_name),
		"per_5": Student.objects.filter(class_per5=s.class_per5).exclude(first_name=first_name, last_name=last_name),
		"per_6": Student.objects.filter(class_per6=s.class_per6).exclude(first_name=first_name, last_name=last_name),
		"per_7": Student.objects.filter(class_per7=s.class_per7).exclude(first_name=first_name, last_name=last_name),
		"per_8": Student.objects.filter(class_per8=s.class_per8).exclude(first_name=first_name, last_name=last_name),
	}
	return render(request, 'tracker/detail.html', {"student": s,"students_in": students_in})
