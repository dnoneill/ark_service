from django.db import models
import arkpy
from django.conf import settings

# Create your models here.
staticurl = "http://127.0.0.1:8000"
class Minter(models.Model):
	name = models.CharField(max_length=1000)
	prefix = models.CharField(max_length=7)
	template = models.CharField(max_length=25)
	active= models.NullBooleanField(null=True)
	date_created = models.DateField(auto_now_add=True)
	description = models.CharField(max_length=1000)
	
	def __repr__(self):
		return "<Minter: {}>".format(self.name)
	
	def _ark_exists(self, key):
		test = Ark.objects.filter(key=key)
		if test.count() == 0:
			return False
		else:
			return True
	def mint(self, quantity=1):
		x = 0
		arks = []
		while x < quantity:
			ark = arkpy.mint(authority=settings.NAAN, template=self.template, prefix=self.prefix)
			if self._ark_exists(ark) == False:
				object = Ark.objects.create(key=ark, minter=self)
				object.bind(staticurl)
				arks.append(ark)
				x +=1	
			else:
				continue
		return arks
class Ark(models.Model):
	key = models.CharField(max_length=25, unique=True) 
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	minter = models.ForeignKey(Minter)
	url = models.URLField(null=True, blank=True)
	
	def __repr__(self):
		return "<Ark: {}>".format(self.key)
	def bind(self, url):
		url = url + "/ark:/" + settings.NAAN + "/" + self.minter.prefix + "/" + self.key
		obj = Ark.objects.get(key=self.key)
		obj.url = url
		obj.save()
		return self.url
		
