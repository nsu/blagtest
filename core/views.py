# Create your views here.
from core.models import *
from django.shortcuts import render
from datetime import datetime
#def list_strings(request):
#   all_strs = StringStore.objects.all()
#    return render(request, 'list_strings.html', {'all_strs':all_strs, 'foo':'other content'})

def add_nums(request, num1, num2):
	result=int(num1)+int(num2)
	return render(request, 'foobar.html', {'result':result})

def mult_nums(request, num1, num2):
	result=int(num1)*int(num2)
	return render(request, 'yet_another_template.html', {'mult_result':result})
def list_posts(request):
	all_posts = Post.objects.all()
	return render(request, 'list_posts.html', {'posts': all_posts, 'today':datetime.now()})