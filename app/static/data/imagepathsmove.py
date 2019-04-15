import json

image_data = {}
with open("pokemondata.json") as json_file:
    data = json.load(json_file)
    for pokemon in data:
     name = pokemon['name'].encode('utf-8')
     image_data[name] = pokemon['imgSrc']


with open('imageslst.json', 'w') as outfile:
    json.dump(image_data, outfile)