from django.db import models

# Create your models here.
class Registration(models.Model):
	course_name = models.CharField(max_length=300 , default="")
	course_dtails = models.CharField(max_length=5000 , default="")
	registration_fee = models.CharField(max_length=30)
	def __str__(self):
		return self.registration_fee

class notice(models.Model):
	name = models.CharField(max_length=300 , default="")
	note = models.CharField(max_length=5000 , default="")
	def __str__(self):
		return self.name
