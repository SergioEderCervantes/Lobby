from django.shortcuts import render

# Create your views here.
def custom_perfil(request):
    return render(request, 'custom_perfil.html', {})