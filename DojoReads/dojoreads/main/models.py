from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-] @[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['name']) < 2:
            errors['name'] = 'Name must be at least 10 characters.'
        if len(postData['alias']) < 2:
            errors['alias'] =  'Alias must be at least 5 characters.'
        if EMAIL_REGEX.match(postData['email']):
            errors['email'] = ('Invalid Email Address')
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match'
        
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        if len(postData['title']) < 1:
            errors['title'] = 'Title is required.'
        if len(postData['author']) < 1:
            errors['author'] = 'Author is required'

        return errors

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}

        if len(postData['review']) < 10:
            errors['review'] = 'Review must be at least 10 characters.'
        
        return errors

class Review(models.Model):
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_reviews', on_delete = models.CASCADE)
    review_of = models.ForeignKey(Book, related_name='book_reviews', on_delete= models.CASCADE)
    objects = ReviewManager()


# Create your models here.
