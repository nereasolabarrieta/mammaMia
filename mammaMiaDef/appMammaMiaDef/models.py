from django.db import models

class Masa(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(('Nombre'),max_length=40)
	def __str__(self):
		return self.nombre

class Ingrediente(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(('Nombre'),max_length=40)
	calorias = models.IntegerField(('Calorias'),default =0)
	def __str__(self):
		return self.nombre

class Pizza(models.Model):
	# No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
	nombre = models.CharField(('Nombre'),max_length=50)
	masa = models.ForeignKey(Masa, on_delete = models.CASCADE)
	precio = models.IntegerField(('Precio'),default =0)
	ingredientes = models.ManyToManyField(Ingrediente)
	def __str__(self):
		return self.nombre