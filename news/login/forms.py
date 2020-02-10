from django import forms

class addnewsForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=200)
    # pub_date = forms.DateTimeField('date published', null=True)