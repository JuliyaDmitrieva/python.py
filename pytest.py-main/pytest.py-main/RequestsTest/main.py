import requests
import pytest 
import json


URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '77e9de4d027aa7d8960ba17af86b85a0'
HEADER= {'trainer_token': TOKEN, 'Content-Type': 'application/json'}
TRAINER_ID = '32964'

body_registration= {
    "name": "Бульбазавр",
    "photo_id": 1
}

response=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_registration)
print(response.text)
pokemon_id = json.loads(response.text).get("id")

body_change={
    "pokemon_id": pokemon_id,
    "name": "ХагиВаги",
    "photo_id": 2
}

response_change=requests.put(url=f'{URL}/pokemons',headers=HEADER, json=body_change)
print(response_change.text)

body_catch={
    "pokemon_id": pokemon_id
}

response_catch=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER, json=body_catch)
print(response_catch.text)