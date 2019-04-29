import json


'''script used to add movesets to existing dataset of pokemon'''


# with open('movedata.json') as json_file:
#     data = json.load(json_file)
#     movesets_data = data

# with open('pokemon_info.json') as json_file:
#     data = json.load(json_file)
#     old_pkmn = data

data_2 = []
with open('pokemondata2.json') as json_file:
    data = json.load(json_file)
    data = data[len(data)/2:]
    for pokemon in data:
      p = {}
      p['imgSrc'] = pokemon['imgSrc']
      p['type1'] = pokemon['type1']
      p['type2'] = pokemon['type2']
      # p['speed'] = pokemon['speed']
      # p['sp_defense'] = pokemon['sp_defense']
      p['moveset'] = pokemon['moveset']
      p['generation'] = pokemon['generation']

      # p['defense'] = pokemon['defense']
      # p['attack'] = pokemon['attack']
      # p['sp_attack'] = pokemon['sp_attack']
      p['name'] = pokemon['name']
      p['legendary'] = pokemon['legendary']
      # p['hp'] = pokemon['hp']
      # p['pokedex_number'] = pokemon['pokedex_number']
      data_2.append(p)



with open('pokemondata4.json', 'w') as outfile:
    json.dump(data_2, outfile)

# with open('pokemondata2.json', 'w') as outfile:
#     json.dump(new_pkmon, outfile)


# with open('missingpokemondata.json', 'w') as outfile:
#     json.dump(missing_pokemon, outfile)