from django.db import models

# Create your models here.
GENDERS = (
		('M', 'male'), 
		('F', 'Female'),
		('N', 'None'),
	)

ROWS = (
	(1, 'ONE'),
	(2, 'TWO'),
	(3, 'THREE'),
	(4, 'FOUR'),
	)
class Student(models.Model):
	sid = models.IntegerField(primary_key=True)
	sname = models.CharField(max_length=100)
	sgender = models.CharField(max_length=6, choices=GENDERS, default='Select')
	srow = models.IntegerField(choices=ROWS, default='Select')
		
	def __str__(self):
		return self.sname

