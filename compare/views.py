from django.shortcuts import render
from .forms import SearchForm
from extApi.models import Tanks

def compare(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            search_results = Tanks.objects.filter(name__icontains = search_query)
            context = {
                'form': form, 
                'query': search_query, 
                'results': search_results
            }
            return render(request, 'compare.html', {'context': context})

    form = SearchForm()
    return render(request, 'compare.html', {'form': form})


#     return render(request, 'deault')

# def search_tank(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search_query = form.cleaned_data['search_suery']
#             return search_query

#     #return render(request, 'compareTanks.html')