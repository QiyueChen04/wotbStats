from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Test

def members(request):
    data = Test.objects.all()
    context = {"tanks": data}
    return render(request, 'tankTable.html', context)