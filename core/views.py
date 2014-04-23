# Create your views here.
from core.models import *
from django.shortcuts import render
from core.forms import *
from datetime import datetime

def test(request):
    testObj = StringStore()
    testObj = 'This is an object being displayed on a web page!'
    return render(request,'test.html',{'test':testObj})
def add_nums(request, num1, num2):
    print "hello"
    a=int(num1)+int(num2)
    s=int(num1)-int(num2)
    m=int(num1)*int(num2)
    d=float(num1)/float(num2)
    return render(request, 'calc.html',{'add':a,'sub':s,'mult':m,'div':d,'one':num1,'two':num2})
def calc(request):
    if request.method=='POST':
        form=Calc(request.POST)
        if form.is_valid():
            num1=form.cleaned_data['num1']
            num2=form.cleaned_data['num2']
            a=int(num1)+int(num2)
            s=int(num1)-int(num2)
            m=int(num1)*int(num2)
            d=float(num1)/float(num2)
            return render(request, 'calc.html',{'add':a,'sub':s,'mult':m,'div':d,'one':num1,'two':num2})
    else:
        form=Calc()
    return render(request,'calculator.html',{'form':form})
def list_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts':all_posts, 'today':datetime.now()})
    
        
    
    
