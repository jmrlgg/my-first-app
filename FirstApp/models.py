from django.contrib import admin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()
# 	#on publisher.object.all() it gives name.
#     def __unicode__(self):
# 	    return self.name
# 	#order by name
#     class Meta:
# 	    ordering = ['name']
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     #on publisher.object.all() it gives first name and last.
#     def __str__(self):
#         return u'%s %s' % (self.first_name, self.last_name)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()
#     #on publisher.object.all() it gives title.
#     def __str__(self):
#         return self.title
#
# class News(models.Model):
#     author = models.CharField(max_length=25)
#     date = models.DateField()
#     title = models.CharField(max_length=150)
#     news = models.TextField(max_length=500)
#     def __unicode__(self):
#         return self.author

# BLOG Addition..


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):
        return self.name


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    joindate = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['joindate']


class Entry(models.Model):
    author = models.OneToOneField(User, db_constraint=False)
    # blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(("Date"), default=date.today)


    def __str__(self):
        return self.headline

    class Meta:
            ordering = ['pub_date']

# image addition
# class Document(models.Model):
#     docfile = models.FileField(upload_to='documents/%Y/%m/%d')
