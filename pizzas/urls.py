from django.urls import path
from .views import PizzaListApi, PizzaDetailApi


urlpatterns = [
    path("pizzas/", PizzaListApi.as_view(), name="pizza-list"),
    path("pizzas/<int:pk>/", PizzaDetailApi.as_view(), name="pizza-detail"),
]
