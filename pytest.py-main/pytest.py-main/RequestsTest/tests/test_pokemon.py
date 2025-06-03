import requests
import pytest

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '77e9de4d027aa7d8960ba17af86b85a0'
HEADER= {'trainer_token': TOKEN, 'Content-Type': 'application/json'}
TRAINER_ID = '32964'

def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name']=='Calypso'
