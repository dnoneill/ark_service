from django.db import models

# Create your models here.

class Minter(models.Model):
	name = models.CharField(max_length=1000)
	prefix = models.CharField(max_length=7)
	template = models.CharField(max_length=25)
	active= models.NullBooleanField(null=True)
	date_created = models.DateField(auto_now_add=True)
	description = models.CharField(max_length=1000)

	def __repr__(self):
		return "Minter: {}".format(self.name)
	
	def _ark_exists(self, key):
		test = Ark.objects.filter(key=key)
		return test

class Ark(models.Model):
	key = models.CharField(max_length=25, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	minter = models.ForeignKey(Minter)
	url = models.URLField(null=True, blank=True)
	
	def __repr__(self):
		return "Ark: {}".format(self.key)