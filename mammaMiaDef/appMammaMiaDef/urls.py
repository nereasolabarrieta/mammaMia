from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pizza/<int:pizza_id>/', views.detailPizza, name='detailPizza'),
	path('masa/<int:masa_id>/', views.detailMasa, name='detailMasa'),
	path('ingrediente/<int:ingrediente_id>/', views.detailIng, name='detailIng'),
	path('pizza/<int:pizza_id>/ingredientes', views.detailIng, name='ingredientesPizza'),
	path('pizzas/', views.pizzas, name='pizzas'),
	path('masas/', views.masas, name='masas'),
	path('ingredientes/', views.ingredientes, name='ingredientes')
]