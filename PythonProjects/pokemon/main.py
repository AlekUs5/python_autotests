import requests

URL='https://api.pokemonbattle.me:9104'

HEADERS={
    "Content-Type": "application/json",
    "trainer_token": "ee7e3a76218a08c92b80a43b0a1614e8"
}
BODY={
    "name": "Cypress",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
PARAMS={"trainer_id": 4584, "alls":1}

message=["Покемон создан", "Ошивка", "Информация о покемоне обновлена", "Покемон пойман в покебол", "Максимум 3 привязанных покемона к покеболу", "Максимум 5 живых покемонов"]

def getPokemons(URL_GET, PARAMS_GET): #Get number trainer's pokemon
    results=[]
    response=requests.get(url=f'{URL_GET}/pokemons', params=PARAMS_GET)
    results=response.json()
    return results


# ###API Создание покемона#####
response = requests.post(url=f'{URL}/pokemons', json=BODY, headers=HEADERS, timeout=5)
if response.status_code==201 and response.json()["message"]==message[0]:
  print(response.json())
elif response.status_code==400 and response.json()["message"]==message[5]:
  print(response.json())
else:
  print(message[1])

# ####API Смена имени покемона#####
a = getPokemons(URL, PARAMS)
for i in range (len(a)): 
    id_pokemon=a[i]['id']
    resp=requests.put(url=f'{URL}/pokemons', json={"pokemon_id": id_pokemon, "name": "Cypress","photo": "https://dolnikov.ru/pokemons/albums/001.png"}, headers=HEADERS, timeout=5)
    if resp.status_code==200 and resp.json()["message"]==message[2]:
        print(resp.json())
    else:
        print(message[1])

# # ###API Поймать покемона в покебол, отвязать покемона#####
b = getPokemons(URL, PARAMS)
for j in range (len(b)):
    if b[j]['in_pokeball']=="0": 
        id_pokemon=b[j]['id']
        added=requests.post(url=f'{URL}/trainers/add_pokeball', json={"pokemon_id":id_pokemon}, headers=HEADERS)
        if added.status_code==200 and added.json()["message"]==message[3]:
            print(added.json())
            break
        elif added.status_code==400 and added.json()["message"]==message[4]:
            print('Превышен лимит')
            id_pok=b[int(((len(b)-1)/2))]['id']
            delete=requests.put(url=f'{URL}/trainers/delete_pokeball', json={"pokemon_id":id_pok}, headers=HEADERS, timeout=5)
            print(delete.json())