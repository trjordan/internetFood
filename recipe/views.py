# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from internetFood.recipe.models import Recipe, Ingredient, Tag

def index(request):
    recipe_list = Recipe.objects.all()
    return render_to_response('index.html', {'recipes': recipe_list})

def detail(request, recipe_id):
    r = get_object_or_404(Recipe, pk=recipe_id)
    return render_to_response('detail.html', {'recipe': r})

