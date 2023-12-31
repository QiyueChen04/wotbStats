from django.shortcuts import render
from . import views

# Create your views here.
def compare_view(request):
    return render(request, 'compareTanks.html')