import requests
from django.shortcuts import render
from .models import Pokemon

#get pokemon data and images from PokeAPI and save to database
def get_pokemon_data():
    for i in range(1, 152):
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
        response = requests.get(url)
        pokemon_data = response.json()
        name = pokemon_data['name'].capitalize()
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        attack = pokemon_data['stats'][4]['base_stat']
        defense = pokemon_data['stats'][3]['base_stat']
        special_attack = pokemon_data['stats'][2]['base_stat']
        special_defense = pokemon_data['stats'][1]['base_stat']
        hp = pokemon_data['stats'][5]['base_stat']
        speed = pokemon_data['stats'][0]['base_stat']
        front_default = pokemon_data['sprites']['front_default']
        back_default = pokemon_data['sprites']['back_default']
        front_shiny = pokemon_data['sprites']['front_shiny']
        back_shiny = pokemon_data['sprites']['back_shiny']
        pokemon = Pokemon(name=name, height=height, weight=weight, attack=attack, defense=defense, special_attack=special_attack, special_defense=special_defense, hp=hp, speed=speed, front_default=front_default, back_default=back_default, front_shiny=front_shiny, back_shiny=back_shiny)
        pokemon.save()

#if model is empty, get data from PokeAPI and save to database
if Pokemon.objects.count() == 0:
    get_pokemon_data()

#render index page
def index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', {'pokemon': pokemon})

#define pokemon_name
def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokedex/pokemon.html', {'pokemon': pokemon})