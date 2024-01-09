from django.shortcuts import render
from .forms import SearchForm
from extApi.models import Tank

def compare(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            search_results = Tank.objects.filter(name__icontains = search_query)
            context = {
                'form': form, 
                'query': search_query, 
                'results': search_results
            }
            return render(request, 'new.html', {'context': context})

    form = SearchForm()
    context = {'form': form}
    return render(request, 'new.html', {'context': context})
