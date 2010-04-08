from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    preperation = models.TextField()
    rating = models.IntegerField()

class Ingredient(models.Model):
    quantity = models.CharField(max_length=200)
    measurement = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)

class Tag(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=200)
