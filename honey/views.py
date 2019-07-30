from django.shortcuts import render

# Create your views here.

def drink(request):
    return render(request, 'drink.html')

def map(request):
    return render(request, 'map.html')

def store(request):
    return render(request, 'store.html')

def toilet(request):
    return render(request, 'toilet.html')


