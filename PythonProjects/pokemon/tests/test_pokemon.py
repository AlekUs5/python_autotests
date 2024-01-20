import requests
import pytest

URL='https://api.pokemonbattle.me:9104'

params={
'level':'1',
'page':'0',
'pokemons_in_pokeballs':'3'
}
def test_get_trainers():
    response=requests.get(url=f'{URL}/trainers', params=params, timeout=5)
    assert response.status_code==200, "Unexpected response code"

#For pytest parametrization
id_trainers=[(4584, "Cypress"), (3608, "Алекс")]
@pytest.mark.parametrize('id, trainer_name', id_trainers) #Fixture
def test_my_trainers_name(id, trainer_name):
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id':id}, timeout=5)
    assert response.json()["trainer_name"]==trainer_name
    assert response.json()["city"] in ['samara', 'Samara']