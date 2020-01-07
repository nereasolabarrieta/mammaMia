from django.contrib import admin
from .models import Pizza, Masa, Ingrediente
#admin.site.register(Pizza)
#admin.site.register(Masa)
#admin.site.register(Ingrediente)

class MasaAdmin (admin.ModelAdmin):
	fields = ['nombre']

admin.site.register(Masa, MasaAdmin)

class IngredienteAdmin (admin.ModelAdmin):
	fields = ['nombre', 'calorias']
	list_display = ['nombre', 'calorias']
	list_filter = ['calorias']

admin.site.register(Ingrediente, IngredienteAdmin)

class PizzaAdmin (admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ['nombre', 'precio']
	fieldsets = [
        (None,               {'fields': ['nombre', 'precio']}),
        ('¿Cómo quieres que sea la pizza?', {'fields': ['masa', 'ingredientes']}),
    ]
    
admin.site.register(Pizza, PizzaAdmin)