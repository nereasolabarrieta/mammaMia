from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Contacto
import sqlite3

from django.http import HttpResponse
from django.utils.translation import ugettext as _
 
#devuelve el listado de empresas
def index(request):
	contactos = get_list_or_404(Contacto.objects.order_by('nombre'))
	context = {'lista_contactos': contactos }
	return render(request, 'index.html', context)