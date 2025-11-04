from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle_videojuego/', views.detalle_videojuego, name='detalle_videojuego'),
    
]