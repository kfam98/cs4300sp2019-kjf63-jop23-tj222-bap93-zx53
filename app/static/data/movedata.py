import json


'''script used to add movesets to existing dataset of pokemon'''

movesets_data = []
image_data = []

missing_pokemon = []

with open('movedata.json') as json_file:
    data = json.load(json_file)
    movesets_data = data


with open('imageData.json') as json_file:
    data = json.load(json_file)
    for pokemon in data:
      if pokemon['name'] in movesets_data.keys():
        pokemon['moveset'] = movesets_data[pokemon['name']]
      else:
        missing_pokemon.append(pokemon['name'])
    image_data = data



with open('pokemondata.json', 'w') as outfile:
    json.dump(image_data, outfile)


with open('missingpokemondata.json', 'w') as outfile:
    json.dump(missing_pokemon, outfile)