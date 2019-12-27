from django.db import models
from django.utils.translation import ugettext_lazy as _

class Masa(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(_('Nombre'),max_length=40)
	def __str__(self):
		return self.nombre

class Ingrediente(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(_('Nombre'),max_length=40)
	calorias = models.IntegerField(_('Calorias'),default =0)
	def __str__(self):
		return self.nombre

class Pizza(models.Model):
	# No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
	nombre = models.CharField(_('Nombre'),max_length=50)
	masa = models.ForeignKey(Masa, on_delete = models.CASCADE)
	precio = models.IntegerField(_('Precio'),default =0)
	ingredientes = models.ManyToManyField(Ingrediente)
	def __str__(self):
		return self.nombre