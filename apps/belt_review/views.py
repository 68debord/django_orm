from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

# Create your views here.
from models import *


def index(request):

	return render(request, 'belt_review/index.html')

def books(request):
	reviews = Review.objects.all().order_by('-created_at')
	listone = []
	i = 0
	for review in reviews:
	
		if i < 3:
			listone.append(review.book.title)
			i += 1

	context = {
	"books": Book.objects.all(),
	"reviews": Review.objects.all().order_by('-created_at'),
	"list": listone
	}
	print listone

	return render(request, 'belt_review/books.html', context)

def bookshow(request, id):





	return render(request, 'belt_review/book_show.html', {"reviews": Review.objects.filter(book_id = id).order_by('-created_at')})	

def user(request, id):
	reviews = Review.objects.filter(reviewer_id=id).order_by('-created_at')	
	books = Book.objects.all()
	# print books
	listone = []
	listtwo = []
	for review in reviews:
		if review.book.title not in listone:
			listone.append(review.book.title)

	for book in books:
		if book.title in listone:
			listtwo.append({"id": book.id, "title": book.title})


	print listone
	# for p in reviews = Review.objects.raw('SELECT book_title FROM book INNER JOIN review ON book_id = review_book_id INNER JOIN user ON user_id = review_reviewer_id WHERE user_id = %s', [id]): 
	# 	print p
	# WHY NO DISTINCT

	return render(request, 'belt_review/user.html', {"reviews": reviews, "length": len(reviews), "list": listtwo})

def add(request):


	return render(request, 'belt_review/book_add.html', {"authors": Author.objects.all()})	

def dualprocess(request):
	if request.POST['newauthor'] == "":
		author = Author.objects.get(name = request.POST['author'])
	else:
		Author.objects.create(name=request.POST['newauthor'])
		author = Author.objects.last()

	Book.objects.create(title=request.POST['title'], author=author)
	book = Book.objects.last()
	reviewer = User.objects.get(id=request.session['id'])

	Review.objects.create(text=request.POST['text'], rating=request.POST['rating'], book=book, reviewer=reviewer)

	return redirect('/belt_review/books/'+str(book.id))

def singleprocess(request, id):
	book = Book.objects.get(id = id)
	reviewer = User.objects.get(id=request.session['id'])

	Review.objects.create(text=request.POST['text'], rating=request.POST['rating'], book=book, reviewer=reviewer)

	return redirect('/belt_review/books/'+str(book.id))

def delete(request, id):
	review = Review.objects.get(id=id)
	review.delete()

	return redirect('/belt_review/books/')

def register(request):

	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/belt_review/')	
		else:
			hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			new_user=User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password = hashed)
			request.session['id'] = new_user.id
			request.session['alias'] = new_user.alias

			return redirect('/belt_review/books/')
	else:
		return redirect('/belt_review/')

def logout(request):
	request.session['id'] = None
	request.session['alias'] = None

	return redirect('/belt_review/')

def login(request):
	if request.method == "POST":
		email = request.POST['email']
		user = User.objects.filter(email=email)
		if len(user) != 0:

			if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
				request.session['id'] = user[0].id
				request.session['alias'] = user[0].alias
			else: 
				messages.error(request, "your password did not match")
				return redirect('/belt_review/')
		else: 
			messages.error(request, "your email was not found")
		
			return redirect('/belt_review/')
		return redirect('/belt_review/books/')

	else:
		return redirect('/belt_review/')

