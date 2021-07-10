from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=10)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
