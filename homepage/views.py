from django.shortcuts import render
from .forms import SearchForm
from extApi.models import *

def homepage(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            tank_results = Tank.objects.filter(name__icontains = search_query)
            context = {
                'form': form, 
                'query': search_query, 
                'tank_results': tank_results,
            }
            return render(request, 'homepage.html', {'context': context})
    form = SearchForm()
    context = {'form': form}
    return render(request, 'homepage.html', {'context': context})

