from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from models import *

def index(request):


	return render(request,'courses/index.html', {"courses": Course.objects.all()})


def create(request):

	if request.method == "POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/courses/')
		else:
			this_desc = Description.objects.create(desc=request.POST['desc'])		
			this_course = Course.objects.create(name=request.POST['name'], desc=this_desc)
			
			# Description.objects.create(course=Course.objects.last(), desc=request.POST['desc'])

			return redirect('/courses/')

	else: 

		return redirect('/courses/')
 

def destroy(request, id):
	if request.method == "POST":
		c = Course.objects.get(id = id)
		c.delete()

		return redirect('/courses/')
	else:
		
		return render(request, 'courses/destroy.html', {'course': Course.objects.get(id = id)})

