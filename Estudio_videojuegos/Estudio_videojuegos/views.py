from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')



# Errores
def mi_error_404(request,exception=None):
    return render(request,'error/404.html',None,None,404)

def mi_error_403(request,exception=None):
    return render(request,'error/403.html',None,None,403)

def mi_error_400(request,exception=None):
    return render(request,'error/400.html',None,None,400)

def mi_error_500(request,exception=None):
    return render(request,'error/500.html',None,None,500)

#Páginas reales
"""En caso de que el titulo del videojuego contenga 'Fantasy' y la sede del estudio de desarrollo esté en un país que contenga 'Unidos', muestra todos los detalles del videojuego, el estudio de desarrollo, las plataformas en las que está disponible y cualquier análisis asociado."""
def detalle_videojuego(request, videojuego_id):
    return render(request, 'detalle_videojuego.html', {'videojuego_id': videojuego_id})
