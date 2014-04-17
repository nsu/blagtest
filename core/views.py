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
def add_nums(request, num1, num2):
    a=int(num1)+int(num2)
    s=int(num1)-int(num2)
    m=int(num1)*int(num2)
    d=float(num1)/float(num2)
    
    return render(request, 'calc.html',{'add':a,'sub':s,'mult':m,'div':d,'one':num1,'two':num2})
def mult_nums(request, num1, num2):
    return render(request, 'calc.html',{'mult':int(num1)*int(num2)})
