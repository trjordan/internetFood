from internetFood.recipe.models import Recipe
from internetFood.recipe.models import Ingredient
from internetFood.recipe.models import Tag
from django.contrib import admin

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
