from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+( [a-zA-Z]+)*$')
# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "name should be more than 2 characters"
        if len(postData['alias']) < 3:
            errors["alias"] = "alias should be more than 2 characters"
        if not NAME_REGEX.match(postData['name']):
        	errors["name"] = "name should be only letters"
        if not NAME_REGEX.match(postData['alias']):
        	errors["alias"] = "alias should be only letters" 
        if not EMAIL_REGEX.match(postData['email']):
        	errors["email"] = "must enter valid email"     
        test = User.objects.filter(email=postData['email'])
        if len(test) != 0:
        	errors["email"] = "email already in use"        	    	
        if len(postData['password']) < 8:
            errors["password"] = "password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
        	errors["password"] = "passwords must match"

        return errors



class Author(models.Model):
	name = models.CharField(max_length=255)	

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = BlogManager()

class Review(models.Model):
	text = models.TextField()
	rating = models.IntegerField()
 	created_at = models.DateTimeField(auto_now_add = True)
 	reviewer = models.ForeignKey(User, related_name="reviews")
 	book = models.ForeignKey(Book, related_name="reviews")