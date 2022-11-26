from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon, name='pokemon'),
    path('team/', views.team, name='team'),

]