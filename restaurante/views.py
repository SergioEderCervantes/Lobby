from django.shortcuts import render

# Create your views here.

def restaurante(request):
    return render(request, 'restaurante.html', {})