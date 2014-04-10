# Create your views here.
from core.models import *
from django.shortcuts import render

def list_strings(request):
    all_strs = StringStore.objects.all()
    return render(request, 'list_strings.html', {'all_strs':all_strs, 'foo':'other content'})
def test(request):
    testObj = StringStore()
    testObj = 'This is an object being displayed on a web page!'
    return render(request,'test.html',{'test':testObj})