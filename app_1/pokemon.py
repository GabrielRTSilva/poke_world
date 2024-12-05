#Importando os objetos Região
from region import lista_r
import requests

class Pokemon():
    def __init__(self, index, name, types, img):
        self.index = index
        self.name = name
        self.type = types
        self.img = img

url_pokedex = [f'https://pokeapi.co/api/v2/pokedex/{regiao.pokedex}/' for regiao in lista_r]
#Faz o request dos nomes dos pokemons. Em seguida, itera sobre a lista_nome para instanciar cada um dos pokemons e adicionar ao atributo Pokemons de cada objeto Region
for url, regiao in zip(url_pokedex, lista_r):
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_pokedex = response.json()
        
        lista_nome = [pokemon['pokemon_species']['name'] for pokemon in dados_pokedex['pokemon_entries']if pokemon['entry_number'] <= 9]
        #lista_nome = [pokemon['pokemon_species']['name'] for pokemon in dados_pokedex['pokemon_entries'] if pokemon['entry_number'] <= 9]

        lista_pokemons = []  # Redefine lista_pokemons para cada região
        
        for nome in lista_nome:
            url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
            response_2 = requests.get(url)
            
            if response_2.status_code == 200:
                dados_pokemon = response_2.json()
                
                params = {
                    'index': dados_pokemon['id'],
                    'name': dados_pokemon['name'],
                    'types': [tipo['type']['name'] for tipo in dados_pokemon['types']],
                    'img': dados_pokemon['sprites']['front_default']
                }
                
                pokemon = Pokemon(**params)
                lista_pokemons.append(pokemon)

        regiao.pokemons = lista_pokemons

