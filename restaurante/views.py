from django.shortcuts import render

def restaurante(request):
    return render(request, 'restaurante.html', {})