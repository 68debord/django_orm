from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['desc']) < 16:
            errors["desc"] = "Course description should be more than 15 characters"
        return errors

class Description(models.Model):
	desc = models.TextField()

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.OneToOneField(Description, related_name="course")
	created_at = models.DateTimeField(auto_now_add = True)
	objects = BlogManager()
