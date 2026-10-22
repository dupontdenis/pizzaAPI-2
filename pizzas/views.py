from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Pizza
from .serializers import PizzaSerializer


class PizzaListApi(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()

        raw = request.query_params.get("ingredients", "")
        mode = request.query_params.get("mode", "or").lower()

        names = [
            name.strip()
            for name in raw.split(",")
            if name.strip()
        ]

        if names:
            if mode == "and":
                for name in names:
                    pizzas = pizzas.filter(
                        ingredients__name=name
                    )
            else:
                pizzas = pizzas.filter(
                    ingredients__name__in=names
                )

            pizzas = pizzas.distinct()

        pizzas = (
            pizzas
            .prefetch_related("ingredients")
            .order_by("id")
        )

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

