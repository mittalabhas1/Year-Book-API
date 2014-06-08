from django.db import models
from users.models import User

class Questions(models.Model):
	"""
	Contains the set of default questions to be asked
	"""
	question = models.CharField(max_length=100)

	def __unicode__(self):
		return self.question

class Answers(models.Model):
	"""
	Contains answers of the questions from the registered users
	"""
	uid = models.ForeignKey(User)
	qid = models.ForeignKey(Questions)
	answer = models.TextField()

	def __unicode__(self):
		return self.uid.username + " (" + self.qid.question + ")"
