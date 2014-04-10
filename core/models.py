from django.db import models

# Create your models here.

class StringStore(models.Model):
    text = models.TextField()
