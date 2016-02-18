from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	grade_choices = (
		("6", "6th Grader"),
		("7", "7th Grader"),
		("8", "8th Grader"),
		("9", "9th Grader"),
		("10", "10th Grader"),
		("11", "11th Grader"),
		("12", "12th Grader")
	)
	grade = models.CharField(max_length=2, choices=grade_choices, default="6")
	#advisory = models.ForeignKey('Advisory', on_delete=models.SET_DEFAULT, default=1, related_name="Advisory+")
	class_per1 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 1443+") #Default is study in Cafe (room #CAF)
	class_per2 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 2+")
	class_per3 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 3+")
	class_per4 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 4+")
	class_per5 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 5+")
	class_per6 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 6+")
	class_per7 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 7+")
	class_per8 = models.ForeignKey('Class', on_delete=models.SET_DEFAULT, default=79, related_name="Period 8+")

	def __str__(self):
		return self.last_name


class Class(models.Model):
	class Meta:
		ordering = ('title',)
	title = models.CharField(max_length=150, blank=False)
	course_number = models.CharField(max_length=20, null=False, blank=False)
	room_per1 = models.CharField(max_length=20, null=True, blank=True)
	room_per2 = models.CharField(max_length=20, null=True, blank=True)
	room_per3 = models.CharField(max_length=20, null=True, blank=True)
	room_per4 = models.CharField(max_length=20, null=True, blank=True)
	room_per5 = models.CharField(max_length=20, null=True, blank=True)
	room_per6 = models.CharField(max_length=20, null=True, blank=True)
	room_per7 = models.CharField(max_length=20, null=True, blank=True)
	room_per8 = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.title

	#Defaults to the default room in each period if other room is not specified
	# @classmethod
	# def create(self, title, default_room, room_per1=None, room_per2=None, room_per3=None, room_per4=None,
	# 	 		room_per5=None, room_per6=None, room_per7=None, room_per8=None):
	# 	self.title = title
	# 	self.room_per1 = default_room or room_per1
	# 	self.room_per2 = default_room or room_per2
	# 	self.room_per3 = default_room or room_per3
	# 	self.room_per4 = default_room or room_per4
	# 	self.room_per5 = default_room or room_per5
	# 	self.room_per6 = default_room or room_per6
	# 	self.room_per7 = default_room or room_per7
	# 	self.room_per8 = default_room or room_per8
	# 	return self
