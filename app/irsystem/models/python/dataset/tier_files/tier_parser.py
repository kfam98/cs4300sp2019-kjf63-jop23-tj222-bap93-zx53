""" File to change the tier-Pokemon json to a Pokemon-tier map"""

import json

def generateTiers():
    with open("tiers.json", newline='') as json_file:
        tier_to_pkmn = json.load(json_file)
        
    pkmn_to_tier = {}
    for tier in tier_to_pkmn:
        for pkmn_name in tier_to_pkmn[tier]:
            pkmn_to_tier[pkmn_name] = tier
            
    with open("pokemon_tiers.json", "w") as fout:
        json.dump(pkmn_to_tier, fout)
        
        
if __name__ == '__main__':
    generateTiers()