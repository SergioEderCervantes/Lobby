from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
class Promocion(object):
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen
def home(request):
    promociones = {
        
            Promocion( "promocion1", static('img/promo.png')),
            Promocion( "promocion2", static('img/promo2.jpg')),
            Promocion( "promocion3", static('img/promo3.jpg')),
            Promocion( "promocion4", static('img/promo4.jpg')),
            Promocion( "promocion5", static('img/promo5.jpg')),
        
    }
    return render(request, 'index.html', {'promociones' : promociones})