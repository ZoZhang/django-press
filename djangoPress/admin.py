from django.contrib import admin

from cocktail.models import Person, Phone, TypePhone, Cocktail, Unit, CocktailIngredientUnite, Ingredient

admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(TypePhone)
admin.site.register(Cocktail)
admin.site.register(Unit)
admin.site.register(CocktailIngredientUnite)
admin.site.register(Ingredient)
