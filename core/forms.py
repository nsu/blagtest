from django import forms

class Calc(forms.Form):
    num1 = forms.CharField(max_length=11)
    num2 = forms.CharField(max_length=11)
    
    