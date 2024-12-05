from django.shortcuts import render

# Create your views here.
def politicas(request):
    return render(request, 'politicas.html', {})