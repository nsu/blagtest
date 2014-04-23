from django.db import models
from django import forms

# Create your models here.

class StringStore(models.Model):
    text = models.TextField()

