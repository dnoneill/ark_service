import json
 
from django.http import HttpResponse, Http404
from django.shortcuts import render
 
from arkapp.models import Ark, Minter

def mint(request):
	minter = Minter(template="template", prefix = "test-")
	minter.save()
	
	return HttpResponse(json.dumps(minter.mint(10)))

def bind(request):
	minter = Minter(template="template", prefix = "test-")
	minter.save()
	ark = Ark()
	ark.minter = minter
	ark.key = minter.mint(1)[0]
	ark.bind("test")
	return HttpResponse(ark)
	
def arks(request):
	arks = [str(ark.key) + "\n" for ark in Ark.objects.all()]
	return HttpResponse(arks)
