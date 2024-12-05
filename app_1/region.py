#Libs
import requests

#Classe Região
class Regiao():
  def __init__(self, index, name, img, description, pokedex, pokemons):
    self.index = index
    self.name = name
    self.img = img
    self.description = description
    self.pokedex = pokedex
    self.pokemons = pokemons

#Lista contendo o nome das regioes
nome_regioes = ['kanto','johto','hoenn','sinnoh','unova','kalos','alola','galar','hisui']

#Lista contendo o número da Pokedex da Região
lista_indexes_pokedexes = [2,3,4,5,8,12,16,27,30]

#Lista contendo as descricoes
descricao_regioes = [' região de Kanto é a primeira introduzida na franquia Pokémon, baseada na região de Kanto no Japão. É conhecida por suas cidades icônicas como Pallet Town, Pewter City e Cerulean City. Kanto é o lar dos primeiros 151 Pokémon, e sua geografia inclui montanhas, florestas e mares. É uma região cheia de nostalgia para muitos fãs da série.',
                     'Johto, localizada a oeste de Kanto, é inspirada nas regiões de Kansai e Chubu do Japão. Conhecida por sua rica cultura e tradições, Johto apresenta cidades como Goldenrod e Ecruteak. A região é famosa por suas lendas envolvendo os Pokémon lendários Ho-Oh e Lugia.',
                     'A região de Hoenn é caracterizada por seu clima tropical e vasta biodiversidade. Inspirada na ilha de Kyushu, no Japão, Hoenn apresenta uma geografia diversificada, com desertos, florestas e oceanos. Cidades notáveis incluem Littleroot e Slateport.',
                     'Sinnoh é conhecida por suas montanhas e clima frio. A região é inspirada na ilha de Hokkaido, no Japão, e apresenta uma rica mitologia envolvendo os Pokémon lendários Dialga, Palkia e Giratina. Cidades importantes incluem Jubilife e Snowpoint.',
                     'Inspirada na cidade de Nova York, Unova é uma região moderna e urbana. É conhecida por suas cidades vibrantes e arranha-céus, como Castelia City. Unova traz uma nova perspectiva ao mundo Pokémon, introduzindo muitos Pokémon únicos e inovadores.',
                     'Kalos é inspirada na França e é conhecida por sua elegância e beleza arquitetônica. A região é famosa pela cidade de Lumiose, um centro cultural e comercial. Kalos introduz a mecânica das Mega Evoluções, trazendo uma nova dimensão ao combate Pokémon.',
                     'Inspirada nas ilhas do Havaí, Alola é uma região composta por várias ilhas tropicais. Conhecida por suas tradições culturais e Pokémon regionais únicos, Alola introduz o conceito de Trials ao invés de ginásios tradicionais. Cidades notáveis incluem Hau-oli e Malie.',
                     'Galar é inspirada no Reino Unido e é conhecida por suas cidades industriais e paisagens rurais. A região apresenta um sistema de ginásios semelhante a estádios esportivos e introduz a mecânica do Dynamax e Gigantamax. Cidades importantes incluem Wyndon e Hammerlocke.',
                     'A região de Hisui é uma versão antiga de Sinnoh, apresentada em "Pokémon Legends: Arceus". É uma terra de mistérios e histórias antigas, onde os jogadores exploram um mundo mais selvagem e menos civilizado, descobrindo as origens da região de Sinnoh.']

#Lista contendo o URL das imagens
img_regioes = ['https://archives.bulbagarden.net/media/upload/thumb/7/7d/PE_Kanto_Map.png/300px-PE_Kanto_Map.png',
               'https://archives.bulbagarden.net/media/upload/thumb/6/64/JohtoMap.png/300px-JohtoMap.png',
               'https://archives.bulbagarden.net/media/upload/thumb/8/85/Hoenn_ORAS.png/300px-Hoenn_ORAS.png',
               'https://archives.bulbagarden.net/media/upload/thumb/0/08/Sinnoh_BDSP_artwork.png/300px-Sinnoh_BDSP_artwork.png',
               'https://archives.bulbagarden.net/media/upload/thumb/f/fc/Unova_B2W2_alt.png/300px-Unova_B2W2_alt.png',
               'https://archives.bulbagarden.net/media/upload/thumb/8/8a/Kalos_alt.png/300px-Kalos_alt.png',
               'https://archives.bulbagarden.net/media/upload/thumb/0/0b/Alola_USUM_artwork.png/300px-Alola_USUM_artwork.png',
               'https://archives.bulbagarden.net/media/upload/thumb/c/ce/Galar_artwork.png/300px-Galar_artwork.png',
               'https://archives.bulbagarden.net/media/upload/thumb/2/22/Legends_Arceus_Hisui.png/300px-Legends_Arceus_Hisui.png']

#Inicializa lista das regioes
lista_r =  []
#Contador
x = 1

#Instancia os objetos apartir do ZIP das listas contendo os parametros
for name, img, description, pokedex in zip(nome_regioes, img_regioes, descricao_regioes, lista_indexes_pokedexes):
  
  #Cria a chave dos parametros para cada um dos objetos Regiao
  params = {
    'index': x,
    'name': name,
    'img': img,
    'description': description,
    'pokedex': pokedex,
    'pokemons': None
  }

  #Conta 1 no index
  x +=1 

  #Istancia os objetos
  regiao = Regiao(**params)
  
  #Adiciona a lista que será rendezerida na rota 
  lista_r.append(regiao)

