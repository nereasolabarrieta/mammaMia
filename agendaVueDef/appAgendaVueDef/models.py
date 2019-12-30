from django.db import models

class Contacto(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(('Nombre'),max_length=40)
	email = models.CharField(('Email'),max_length=40)
	telefono = models.CharField(('Telefono'),max_length=40)
	def __str__(self):
		return self.nombre