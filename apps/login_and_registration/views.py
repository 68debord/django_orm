from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

# Create your views here.
from models import *

def index(request):

	return render(request, 'login_and_registration/index.html')

def register(request):

	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/login_and_registration/')	
		else:
			hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			new_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password = hashed)
			request.session['id'] = new_user.id
			request.session['first_name'] = new_user.first_name

			return redirect('/login_and_registration/success/')
	else:
		return redirect('/login_and_registration/')

def login(request):
	if request.method == "POST":
		email = request.POST['email']
		user = User.objects.filter(email=email)
		if len(user) != 0:

			if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
				request.session['id'] = user[0].id
				request.session['first_name'] = user[0].first_name
			else: 
				messages.error(request, "your password did not match")
				return redirect('/login_and_registration/')
		else: 
			messages.error(request, "your email was not found")
		
			return redirect('/login_and_registration/')
		return redirect('/login_and_registration/success/')

	else:
		return redirect('/login_and_registration/')

def success(request):

	return render(request, 'login_and_registration/success.html')