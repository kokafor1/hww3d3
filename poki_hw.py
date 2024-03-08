import requests

class Pokemon:
    def __init__(self,poke_id, name, height, weight):
        self.id = poke_id
        self.name = name.title()
        self.height = height
        self.weight = weight
    
    def __repr__(self):
        return f'<Pokemon {self.id}|{self.name}'

class PokeAPI:
    base_url = "https://pokeapi.co/api/v2/"

    def __get(self, endpoint, id_name):
        requests_url = self.base_url + endpoint + '/' + id_name
        response = requests.get(requests_url)
        if response.ok:
            return response.json()
        else:
            return None   
        
    def get_pokemon(self, poke_name):
        data = self.__get('pokemon', poke_name.lower())
        if data:
            poke_id = data.get('id')
            name = data.get('name')
            height = data.get('height')
            weight = data.get('weight')
        else:
            print(f'No pokemon named {poke_name}')

client = PokeAPI()

while True:
    poke = input('Enter Pokemon name: ')
    if poke == 'quit':
        break
    pokemon = client.get_pokemon(poke)
    print(pokemon)