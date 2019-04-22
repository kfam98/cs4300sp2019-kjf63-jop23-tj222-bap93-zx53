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


with open('pokemondata2.json') as json_file:
    data = json.load(json_file)
    for pokemon in data:
      if "type1" in pokemon.keys() and "type2" in pokemon.keys():
          type1 = pokemon['type1']
          type2 = pokemon['type2']
          if type2 == None:
            type2 = ''
          pokemon_lst[pokemon['name']] = {'type1': type1, 'type2':type2}


with open('typeslst.json', 'w') as outfile:
    json.dump(pokemon_lst, outfile)

# with open('pokemondata2.json', 'w') as outfile:
#     json.dump(new_pkmon, outfile)


# with open('missingpokemondata.json', 'w') as outfile:
#     json.dump(missing_pokemon, outfile)