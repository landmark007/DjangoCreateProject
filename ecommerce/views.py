from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ho Bro")

def input(request, item_id, name):
    return render(request, 'index.html')

def table(request):
    return render(request, 'table.html')

def pokemon(request):
    return render(request, 'pokemon.html')