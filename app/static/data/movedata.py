import json


'''script used to add movesets to existing dataset of pokemon'''

movesets_data = []
old_pkmn = []
new_pkmon = []

missing_pokemon = []

pokemon_lst = []

with open('movedata.json') as json_file:
    data = json.load(json_file)
    movesets_data = data

with open('pokemon_info.json') as json_file:
    data = json.load(json_file)
    old_pkmn = data


with open('pokemondata.json') as json_file:
    data = json.load(json_file)
    for pokemon in data:
      if pokemon['name'] in movesets_data.keys():
        pokemon['moveset'] = movesets_data[pokemon['name']]
        pokemon_lst.append(pokemon['name'])
      else:
        missing_pokemon.append(pokemon['name'])

      if pokemon['name'] in old_pkmn.keys():
        name = pokemon['name']
        pokemon['attack'] = old_pkmn[name]['attack']
        pokemon['defense'] = old_pkmn[name]['defense']
        pokemon['hp'] = old_pkmn[name]['hp']
        pokemon['sp_attack'] = old_pkmn[name]['sp_attack']
        pokemon['sp_defense'] = old_pkmn[name]['sp_defense']
        pokemon['speed'] = old_pkmn[name]['speed']
        pokemon['type1'] = old_pkmn[name]['type1']
        pokemon['type2'] = old_pkmn[name]['type2']
        # pokemon['generation'] = old_pkmn[name]['generation']
    new_pkmon = data




with open('pokemondata2.json', 'w') as outfile:
    json.dump(new_pkmon, outfile)


with open('missingpokemondata.json', 'w') as outfile:
    json.dump(missing_pokemon, outfile)