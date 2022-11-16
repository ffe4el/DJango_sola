from django import forms

class ArticleForm(forms.Form):

    titile = forms.CharField()

    content = forms.CharField(widget=forms.Textarea)