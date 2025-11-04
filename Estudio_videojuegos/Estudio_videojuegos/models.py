from django.db import models

# Create your models here.

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
    
