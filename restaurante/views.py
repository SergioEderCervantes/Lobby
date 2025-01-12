from django.shortcuts import render
from .models import Producto, Seccion_productos, Subseccion_Productos
# Create your views here.
class Section():
    def __init__(self, title = "", subsections = [], imagen1 = None, imagen2 = None):
        self.section_title = title
        self.subsections = subsections
        self.imagen1 = imagen1
        self.imagen2 = imagen2
    def append_subsection(self, subsection):
        self.subsections.append(subsection)
        
class Subsection():
    def __init__(self, nombre = "", es_visible = True,  productos = []):
        self.nombre_subseccion = nombre if es_visible else ""
        self.productos = productos
             
        
def restaurante(request):
    # Corazones
    usuario = request.user
    
    num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0 
    
    # Agarrar todas las secciones y sus productos
    secciones = Seccion_productos.objects.all()  
    menu_sections = []

    for seccion in secciones:
        aux = Section(seccion.nombre_seccion, [], seccion.imagen_respaldo_1, seccion.imagen_respaldo_2)
        subsecciones = Subseccion_Productos.objects.filter(seccion_producto=seccion).order_by('-es_visible')
        for subseccion in subsecciones:
            productos = Producto.objects.filter(subseccion = subseccion)
            aux.append_subsection(Subsection(subseccion.nombre_subseccion, subseccion.es_visible, productos))
        
        menu_sections.append(aux)
    
    context = {
        "menu_sections": menu_sections,
        "num_torneos_inscritos": num_torneos_inscritos,
    }

    return render(request, 'restaurante.html', context)


def prueba(request):
    return render(request, "prueba.html", {})