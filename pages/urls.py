from django.urls import path
from . import views

urlpatterns = [
    path('price', views.price, name='price'),
    path('games', views.games, name='games'),
    path('elements', views.elements, name='elements'),
]
