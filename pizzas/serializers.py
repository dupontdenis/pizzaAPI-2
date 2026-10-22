from rest_framework import serializers
from .models import Pizza, Ingredient




class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "price", "calories"]




class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)


    class Meta:
        model = Pizza
        fields = ["id", "name", "ingredients"]
