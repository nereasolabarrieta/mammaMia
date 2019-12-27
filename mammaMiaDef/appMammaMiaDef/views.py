from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Pizza, Masa, Ingrediente
import sqlite3

from django.http import HttpResponse
from django.utils.translation import ugettext as _
 
#devuelve el listado de empresas
def index(request):
	masas = get_list_or_404(Masa.objects.order_by('nombre'))
	pizzas = Pizza.objects.raw('SELECT * FROM( SELECT * FROM appMammaMiaDef_Pizza ORDER BY precio DESC) GROUP BY masa_id ')
	
	context = {'lista_pizzas': pizzas, 'lista_masas': masas}
	return render(request, 'index.html', context)

def pizzas(request):
	pizzas = get_list_or_404(Pizza.objects.order_by('nombre'))
	context = {'lista_pizzas': pizzas }
	return render(request, 'pizzas.html', context)

def masas(request):
	masas = get_list_or_404(Masa.objects.order_by('nombre'))
	context = {'lista_masas': masas }
	return render(request, 'masas.html', context)

def ingredientes(request):
	ingredientes = get_list_or_404(Ingrediente.objects.order_by('nombre'))
	context = {'lista_ingredientes': ingredientes }
	return render(request, 'ingredientes.html', context)

def detailPizza(request, pizza_id):
	pizza = get_object_or_404(Pizza, pk=pizza_id)
	ingredientes = pizza.ingredientes.all()
	context = {'pizza': pizza, 'lista_ingredientes': ingredientes }
	return render(request, 'detailPizza.html', context)

def detailMasa(request, masa_id):
	masa = get_object_or_404(Masa, pk=masa_id)
	pizzas = masa.pizza_set.all()
	context = {'masa': masa , 'pizzas' : pizzas}
	return render(request, 'detailMasa.html', context)

def detailIng(request, ingrediente_id):
	ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
	pizzas = ingrediente.pizza_set.all()
	context = {'pizzas': pizzas,'ingrediente': ingrediente}
	return render(request, 'detailIng.html', context)