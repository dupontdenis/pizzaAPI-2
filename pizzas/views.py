from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Pizza
from .serializers import PizzaSerializer


class PizzaListApi(APIView):
    def get(self, request):
        pizzas = (
            Pizza.objects
            .prefetch_related("ingredients")
            .order_by("id")
        )


        raw = request.query_params.get("ingredients", "")
        mode = request.query_params.get("mode", "or").lower()


        if raw:
            names = [
                name.strip()
                for name in raw.split(",")
                if name.strip()
            ]


            if names:
                filtered_pizzas = []


                for pizza in pizzas:
                    ingredient_names = [
                        ingredient.name
                        for ingredient in pizza.ingredients.all()
                    ]


                    if mode == "and":
                        matches = all(
                            name in ingredient_names
                            for name in names
                        )
                    else:
                        matches = any(
                            name in ingredient_names
                            for name in names
                        )


                    if matches:
                        filtered_pizzas.append(pizza)


                pizzas = filtered_pizzas


        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)




class PizzaDetailApi(APIView):
    def get(self, request, pk):
        pizza = get_object_or_404(
            Pizza.objects.prefetch_related("ingredients"),
            pk=pk,
        )


        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

