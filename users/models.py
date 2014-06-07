from django.db import models

class User(models.Model):
	"""
	This class contains the user login information ie username and password
	"""
	username = models.CharField(max_length = 20, blank = False)
	password = models.CharField(max_length = 50, blank = False)

	def __unicode__(self):
		return self.username

class UserDetails(models.Model):
	"""
	This class contains all the personal and public information of the user ie name, email address, phone no, dob, hometown, etc
	"""
	uid = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	course = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	phoneNo = models.IntegerField(max_length=15)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	hometown = models.CharField(max_length=50)
	

	def __unicode__(self):
		return self.name