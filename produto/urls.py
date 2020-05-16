from django.urls import path, include
from .views import lista_produtos


urlpatterns = [
    path('', lista_produtos),
]