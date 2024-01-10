from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label = 'Search by name', max_length = 100)