# Create your views here.
from core.models import *
from django.shortcuts import render
from datetime import datetime

def add_nums(request, num1, num2):
    pass

def list_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': all_posts, 'today':datetime.now()})
