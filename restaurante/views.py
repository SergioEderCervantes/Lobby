from django.shortcuts import render
from .models import Producto, Seccion_productos
# Create your views here.
class Section():
    def __init__(self, title = "", products = [], imagen1 = None, imagen2 = None):
        self.section_title = title
        self.products = products
        self.imagen1 = imagen1
        self.imagen2 = imagen2
        
        
def restaurante(request):
    # Corazones
    usuario = request.user
    
    num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0 
    
    # Agarrar todas las secciones y sus productos
    secciones = Seccion_productos.objects.all()  # Asegúrate de que `Seccion` sea el nombre del modelo relacionado
    menu_sections = []

    for seccion in secciones:
        productos = Producto.objects.filter(seccion_producto=seccion)
        menu_sections.append(Section(seccion.nombre_seccion, productos, seccion.imagen_respaldo_1, seccion.imagen_respaldo_2))
    
    context = {
        "menu_sections": menu_sections,
        "num_torneos_inscritos": num_torneos_inscritos,
    }

    return render(request, 'restaurante.html', context)


def prueba(request):
    return render(request, "prueba.html", {})