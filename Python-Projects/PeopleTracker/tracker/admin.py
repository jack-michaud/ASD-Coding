from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	class Meta:
		ordering = ['last_name']
	fieldsets = [
		('Name', 	{"fields":['first_name', 'last_name']}),
		(None, 		{"fields":['grade']}), 
		("Classes", {"fields":[
							'class_per1', 'class_per2', 'class_per3', 'class_per4'
							, 'class_per5', 'class_per6', 'class_per7', 'class_per8'
						]
					}	
		)
	]
	search_fields = ['last_name', 'first_name']
	list_display = ['last_name','first_name', 'grade']

class ClassAdmin(admin.ModelAdmin):
	fieldsets = [
		("Course Title", {"fields": ['title', 'course_number']}),
		("Rooms", {"fields": ['room_per1', 'room_per2', 'room_per3', 'room_per4'
					, 'room_per5', 'room_per6', 'room_per7', 'room_per8']
				}
		)
	]
	search_fields = ['title', 'course_number']
	list_display = ['title', 'course_number']
	
	class Meta:
		ordering = ['title']

admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
