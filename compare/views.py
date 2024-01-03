from django.shortcuts import render
from .forms import SearchForm

def compare(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            #search_results = YourModelName.objects.filter(field_name__icontains=search_query)
            return render(request, 'compare.html', {'query': search_query})

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