import csv
import ast



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
    
    """
    
    
    
    def __init__(self, name, pkdex_num, att, defs, hp, spd, sp_att, sp_def,
                 gen, capture_rate, type1, type2 = None, is_legendary = False, abilities = []):
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
        abilities: The abilities the pokemon could have [list of strings]
        type1: The primary type of the pokemon [string]
        type2: The secondary type of the pokemon [string or None]
        is_legendary: Whether this pokemon is a legendary or not [bool]
        
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
        self.abilities = abilities
        self.type1 = type1
        self.type2 = type2
        self.is_legendary = is_legendary
        
        
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
    
    with open("app/data/pokemon_cleaned.csv", newline = '') as csv_file:
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
    with open("app/data/pokemon.csv", newline = '') as csv_file2:
        csv_reader = csv.reader(csv_file2, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                name = row[30]
                abilities = ast.literal_eval(row[0])
                result[name].abilities = abilities
            
            line_count += 1
            
    return result
        


if __name__ == "__main__":
    print(generate_instances())
    
        
        
        
        
        
        
        
        
        
        
        
        