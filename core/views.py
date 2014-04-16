# Create your views here.
from core.models import *
from django.shortcuts import render

def list_strings(request):
    all_strs = StringStore.objects.all()
    return render(request, 'list_strings.html', {'all_strs':all_strs, 'foo':'other content'})

def add_nums(request, num1, num2):
    a = int(num1) + int (num2)
    return render(request, 'calc_result.html', {'result':a})
