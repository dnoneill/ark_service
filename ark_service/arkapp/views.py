import json
 
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
 
from arkapp.models import Ark, Minter

def homepage(request):
	return render(request, "homepage.html", {})
	
def mint(request):
	number = request.GET.get("mint")
	minter = request.GET.get("minter")
	try:
		mint_obj = Minter.objects.get(pk=minter)
	except:
		return HttpResponseRedirect("http://127.0.0.1:8000")
	mint = mint_obj.mint(int(number))
	return HttpResponse(json.dumps(mint))

def bind(request):
	url = request.GET.get("bind")
	ark = request.GET.get("ark")
	try:
		ark_obj = Ark.objects.get(pk=ark)
	except:
		return HttpResponseRedirect("http://127.0.0.1:8000")
	oldurl = ark_obj.url
	bind = ark_obj.bind(url)
	urls = {"Old URL":oldurl, "New URL":bind}
	return HttpResponse(json.dumps(urls))
	
def resolve(request):
	ark = request.GET.get("resolve")
	try:
		ark_obj = Ark.objects.get(pk=ark)
	except:
		return HttpResponseRedirect("http://127.0.0.1:8000")
	url = str(ark_obj.url)
	if "http://" not in url:
		url = "http://" + url
	else:
		url = url
	return HttpResponseRedirect(url)
