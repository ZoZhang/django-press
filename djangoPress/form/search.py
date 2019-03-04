from django import forms

from djangoPress.model.article import Article


class FormSearch(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title']




