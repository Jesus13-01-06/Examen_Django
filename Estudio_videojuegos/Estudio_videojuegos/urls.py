from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videojuego/<int:videojuego_id>/', views.detalle_videojuego, name='detalle_videojuego'),
]