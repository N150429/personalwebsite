from django.db import models
from phone_field import PhoneField
# Create your models here.
class about(models.Model):
	first_name = models.CharField(max_length=150,blank=False)
	last_name = models.CharField(max_length=150,blank=False)
	address_line1 = models.CharField(max_length=200,blank=True)
	address_line2 = models.CharField(max_length=200,blank=True)
	phone = PhoneField(null=True,blank=True, help_text='Contact phone number')
	email = models.EmailField(max_length=254,blank=False)
	description = models.TextField(max_length=300,blank=False)
	profile  =models.ImageField(null=True,blank=True,upload_to="img/")
class projects(models.Model):
	title = models.CharField(max_length=150,blank=True)
	skills = models.CharField(max_length=256,blank=True)
	start_date = models.DateField(blank=True)
	workmode = models.BooleanField()
	end_date = models.DateField(null=True, blank=True)
	description = models.TextField(max_length=300, blank=True)
	link = models.URLField(max_length = 200,null=True,blank=True)

class education(models.Model):
	title = models.CharField(max_length=150,blank=True)
	stream = models.CharField(max_length=256,blank=True)
	start_date = models.DateField(null=True,blank=True)
	end_date = models.DateField(null=True, blank=True)
	gpa=models.FloatField(null=False)

class skills(models.Model):
	title = models.CharField(max_length=30)
class skillset(models.Model):
	lists = models.ManyToManyField(skills)

class interest(models.Model):
	description = models.TextField(max_length=300)
class awardandcertifications(models.Model):
	title = models.CharField(max_length=200,blank=True)
	link = models.URLField(max_length=250,null=True,blank=True)
class organizations(models.Model):
	title = models.CharField(max_length=150,blank=True)
	start_date = models.DateField(blank=True)
	workmode = models.BooleanField()
	end_date = models.DateField(null=True, blank=True)
	description = models.TextField(max_length=300, blank=True)
class worksamples(models.Model):
	sample = models.CharField(max_length=256,blank=True,null=False)
	link = models.URLField(max_length=250,blank=True,null=False)

class resume(models.Model):
	resume  = models.FileField(upload_to='')