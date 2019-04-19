import csv
import ast
import json
from .constants import *
import os

class Pokemon():

    """ A class to represent an instance of a Pokemon

    INSTANCE ATTRIBUTES:
        name: The Pokemon's name [string]
        pokedex_num: The pokedex number of the pokemon [int]
        attack: The attack stat of the pokemon [int]
        defense: The defense stat of the pokemon [int]
        hp: The hp stat of the pokemon [int]
        speed: The speed stat of the pokemon [int]
        sp_attack: The special attack stat of the pokemon [int]
        sp_defense: The special defense stat of the pokemon [int]
        gen: The generation of the pokemon [int]
        capture_rate: the capture rate of the pokemon as a percentage [float]
        abilities: The abilities the pokemon could have [list of strings]
        type1: The primary type of the pokemon [string]
        type2: The secondary type of the pokemon [string or None]
        is_legendary: Whether this pokemon is a legendary or not [bool]
        weaknesses: Types this pokemon is weak to [set of strings]
        resistances: Types this pokemon resists [set of strings]
        immunities: Types this pokemon is immune to [set of strings]

    """



    def __init__(self, name, pkdex_num, att, defs, hp, spd, sp_att, sp_def,
                 gen, capture_rate, type1, type2 = None, is_legendary = False,):
        """ Initializer for the Pokemon class

        Parameters:
        name: The Pokemon's name [string]
        pkdex_num: The pokedex number of the pokemon [int]
        att: The attack stat of the pokemon [int]
        defs: The defense stat of the pokemon [int]
        hp: The hp stat of the pokemon [int]
        spd: The speed stat of the pokemon [int]
        sp_att: The special attack stat of the pokemon [int]
        sp_def: The special defense stat of the pokemon [int]
        gen: The generation of the pokemon [int]
        capture_rate: the capture rate of the pokemon (out of 255) [int]
        type1: The primary type of the pokemon [string]
        type2: The secondary type of the pokemon [string or None]
        is_legendary: Whether this pokemon is a legendary or not [bool]
        tier: The competitive tier of the pokemon [string]

        """

        self.name = name
        self.pokedex_num = pkdex_num
        self.attack = att
        self.defense = defs
        self.hp = hp
        self.speed = spd
        self.sp_attack = sp_att
        self.sp_defense = sp_def
        self.gen = gen
        self.capture_rate = round((100 * capture_rate/3)/255 , 1)
        self.abilities = []
        self.type1 = type1
        self.type2 = type2
        self.is_legendary = is_legendary
        self.weaknesses = []
        self.resistances = []
        self.immunities = []
        self.tier = ""



    def get_base_total(self):
        """ Returns the base total of this Pokemon """

        return (self.attack + self.defense + self.hp + self.speed + self.sp_attack +
                self.sp_defense)


    def __str__(self):
        if self.type2 == None:
            return ("Name: " + self.name + ", Type: " + self.type1)
        else:
            return ("Name: " + self.name + ", Type: " + self.type1 + '/' + self.type2)





def generate_instances():
    """ Function to generate Pokemon instances of all Pokemon in the pokemon dataset.
    Returns a dictionary of Pokemon name to its Pokemon instance """

    result =  {}

    path = os.path.dirname(os.path.realpath(__file__))

    with open(path+"/dataset/pokemon_cleaned.csv", newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                name = row[0]
                att = int(row[1])
                capt_score = int(row[2])
                defs = int(row[3])
                hp = int(row[4])
                pkdex_num = int(row[5])
                sp_att = int(row[6])
                sp_def = int(row[7])
                spd = int(row[8])
                type1 = row[9]

                if row[10] == '':
                    type2 = None
                else:
                    type2 = row[10]

                gen = int(row[11])
                is_legendary = bool(int(row[12]))

                result[name] = Pokemon(name,pkdex_num,att,defs,hp,spd,sp_att,sp_def,
                                       gen, capt_score,type1,type2, is_legendary)
            line_count += 1

    # Need to get pokemon abilities from the main pokemon csv
    with open(path+"/dataset/pokemon.csv", newline = '') as csv_file2:
        csv_reader = csv.reader(csv_file2, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                name = row[30]
                abilities = ast.literal_eval(row[0])
                result[name].abilities = abilities


                matchups = row[1:19]
                for i in range(len(matchups)):
                    if float(matchups[i]) > 1.0:
                        result[name].weaknesses.append(PTYPES[i])
                    elif float(matchups[i]) == 0:
                        result[name].immunities.append(PTYPES[i])
                    elif float(matchups[i]) < 1.0:
                        result[name].resistances.append(PTYPES[i])

            line_count += 1


    with open(path+"/dataset/pokemon_tiers.json", newline = '') as json_file:
        tier_dict = json.load(json_file)

    for pkmn_name in result:
        result[pkmn_name].tier = tier_dict[pkmn_name]

    return result

def generateTypeChart():
    """ Returns the overall Pokemon type chart as a dictionary.

    The key k represents the attacking type, and the value is a list of numbers.
    For any value v in the list at position x, it means that type k is v times as
    effective towards type types[x], where types is the global variable of types. """

    result = {}
    path = os.path.dirname(os.path.realpath(__file__))

    with open(path+"/dataset/chart.csv", newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                result[row[0].lower()] = list(map(float,row[1:]))

            line_count += 1

        return result


def generatePokemonMoves():
    """ Returns a dictionary where each key is a string identifying a specific
        Pokemon, and its value is a string list of all moves which can be
        learned by that Pokemon through leveling up, breeding, or a machine. """
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path+"/dataset/movedata.json", newline = '') as json_file:
        result = json.load(json_file)
    return result

def generateMoveData():
    """ Returns a dictionary where each key is a string identifying a specific
        move, and its value is the type of the move. """
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path+"/dataset/allmove_data.json", newline = '') as json_file:
        result = json.load(json_file)
    return result

# Global variable with type chart
type_chart = generateTypeChart()
pkmn_moves = generatePokemonMoves()
move_types = generateMoveData()

if __name__ == "__main__":
    print(generate_instances())
    # for i in range(len(types)):
    #     print('Dark is ' + str(type_chart['dark'][i]) + ' times effective towards ' + types[i] )
