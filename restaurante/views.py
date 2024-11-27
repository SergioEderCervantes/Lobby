from django.shortcuts import render
from .models import Producto
# Create your views here.
class Section():
    def __init__(self, title = "", products = []):
        self.section_title = title
        self.products = products
        
        
def restaurante(request):
    #Agarrar todos los productos
    productos = Producto.objects.all()
    context = {
        "menu_sections" : [
            Section("Comida", [product for product in productos if product.tipo_producto == 'A']),
            Section("Bebida sin Alcohol", [product for product in productos if product.tipo_producto == 'B']),
            Section("Cervezas", [product for product in productos if product.tipo_producto == 'C']),
            Section("Bebidas con alcohol", [product for product in productos if product.tipo_producto == 'D']),
            Section("Botellas", [product for product in productos if product.tipo_producto == 'E']),
        ]
    }
    return render(request, 'restaurante.html', context)