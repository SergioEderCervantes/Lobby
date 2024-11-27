from django.shortcuts import render

# Create your views here.
def cookies_servicios(request):
    return render(request, 'cookies_servicios.html', {})