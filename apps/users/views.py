from django.shortcuts import render, redirect

from models import *

# Create your views here.

def index(request):

	return render(request, "users/index.html", {"users": User.objects.all()})

def new(request):

	return render(request, "users/new_user.html")

def edit(request, id):
	context = {'user_id': id}
	return render(request, "users/user_edit.html", context)

def show(request, id):

	return render(request, "users/user_show.html", {"user": User.objects.get(id = id)})

def destroy(request, id):
	u = User.objects.get(id = id)
	u.delete()

	return redirect("/users/")


def create(request):
	if request.method == "POST":
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])

		u = User.objects.last()
		id = u.id
			
		return redirect('/users/'+str(id))

	else:
		return redirect('/users/')

def update(request, id):
	if request.method == "POST":

		u = User.objects.get(id = id)
		u.first_name = request.POST['first_name']
		u.last_name = request.POST['last_name']
		u.email = request.POST['email']
		u.save()

			
		return redirect('/users/')

	else:
		return redirect('/users/')