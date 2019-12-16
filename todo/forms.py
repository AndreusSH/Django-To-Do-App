from django import forms
    
class AddTask(forms.Form):
    text = forms.CharField(max_length=4000, required=False)
