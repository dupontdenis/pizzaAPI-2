from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()


    def __str__(self):
        return self.name




class Pizza(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="pizzas",
        blank=True,
    )


    def __str__(self):
        return self.name
