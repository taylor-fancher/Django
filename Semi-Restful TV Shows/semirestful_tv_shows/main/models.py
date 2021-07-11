from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title must be as least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description must be at least 10 characters'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=10)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

# Create your models here.
