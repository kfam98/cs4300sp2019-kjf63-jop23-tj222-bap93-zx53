import json


'''script used to add movesets to existing dataset of pokemon'''

movesets_data = []
old_pkmn = []
new_pkmon = []

missing_pokemon = []

pokemon_lst = {}

# with open('movedata.json') as json_file:
#     data = json.load(json_file)
#     movesets_data = data

# with open('pokemon_info.json') as json_file:
#     data = json.load(json_file)
#     old_pkmn = data

image_lst = {}


with open('pokemondata2.json') as json_file:
    data = json.load(json_file)
    for pokemon in data:
      image_lst[pokemon['name']] = pokemon['imgSrc']


with open('imageslst.json', 'w') as outfile:
    json.dump(image_lst, outfile)

# with open('pokemondata2.json', 'w') as outfile:
#     json.dump(new_pkmon, outfile)


# with open('missingpokemondata.json', 'w') as outfile:
#     json.dump(missing_pokemon, outfile)