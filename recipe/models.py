from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    preparation = models.TextField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.title

class Ingredient(models.Model):
    quantity = models.CharField(max_length=200)
    measurement = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return self.quantity + ' ' + self.measurement + ' ' + self.ingredient

class Tag(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=200)
