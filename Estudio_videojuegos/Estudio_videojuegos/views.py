from django.shortcuts import render


# Create your views here.
"""Dada la siguiente SQL, crea los Modelos, Urls y QuerySets correspondientes para mostrar los datos que se piden:

SELECT 
    V.*,E.*,VP.*,P.*
FROM 
    videojuego V
INNER JOIN 
    estudio E ON V.estudio_desarrollo_id = E.id
INNER JOIN 
    sede S ON E.id = S.estudio_id
LEFT JOIN 
    videojuego_plataformas VP ON V.id = VP.videojuego_id
LEFT JOIN
    plataforma P ON VP.plataforma_id = P.id
LEFT JOIN
    analisis A ON V.id = A.videojuego_id
WHERE 
    V.titulo LIKE '%Fantasy%' 
    AND S.pais LIKE '%Unidos%';
"""
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

def detalle_videojuego(request, videojuego_id):
    # Lógica para obtener los detalles del videojuego con el ID proporcionado
    contexto = {
        'videojuego_id': videojuego_id,
        # Agrega más datos al contexto según sea necesario
    }
    return render(request, 'detalle_videojuego.html', contexto)