# Create your views here.
from core.models import *
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from forms import PostForm

def add_nums(request, num1, num2):
    a = int(num1) + int(num2)
    return render(request, 'calc_result.html', {'result':a})

def mult_nums(request, num1, num2):
    a = int(num1) * int(num2)
    return render(request, 'calc_result.html', {'result':a})

def list_posts(request):
	all_posts = Post.objects.all()
	return render(request, 'list_posts.html', {'all_posts':all_posts, 'today':datetime.now()})

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/blag/list')
	else:
		form = PostForm()
	return render(request, 'new_post.html', {'form':form})
