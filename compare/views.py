from django.shortcuts import render
from .forms import SearchForm
from extApi.models import *

def compare(request, tank_name1, tank_name2):
    if(tank_name2 == ""):
        tank1 = Tank.objects.filter(name= tank_name1)
        context = {
            'form': SearchForm(request.GET),
            'tanks': tank1
        }
        return render(request, 'compare.html', {'context': context})
    else:
        pass


# def compare(request, tank_name1, tank_name2):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search_query = form.cleaned_data['search_query']
#             tank_results = Tank.objects.filter(name__icontains = search_query)
#             context = {
#                 'form': form, 
#                 'query': search_query, 
#                 'tank_results': tank_results,
#             }
#             return render(request, 'new.html', {'context': context})

#     form = SearchForm()
#     context = {'form': form}
#     return render(request, 'new.html', {'context': context})
