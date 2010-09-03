from django.db import models

# Create your models here.
class Contact(models.Model):

	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

# Create your models here.
class Employer(models.Model):

	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name
