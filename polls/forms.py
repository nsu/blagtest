from django import forms
from polls.models import *

class PollForm(forms.ModelForm):
    class Meta:
        model=Poll
        exclude = ['pub_date']
class ChoiceForm(forms.ModelForm):
    class Meta:
        model=Choice
        exclude = ['poll','votes']