from constants import *
# At this stage, we should know which of the opponent's Pokemon are not countered
# by any of the current team

# Want to find pokemon to add to current team that counter the rest of the opponent's team


def generateScore(pkmn, playstyle, pkmn_weights):
    """ Returns a score for the pkmn to be used for ranking, based on the playstyle
    
    Parameters:
    pkmn: The Pokemon instance [pokemon.Pokemon instance]
    playstyle: One of "balanced", "defensive" or "glass-cannon"
    pkmn_weights: Dictionary of pokemon social weights [dict of ints]
    
    """
    atk = PLAYSTYLES[playstyle][ATTACK]
    defs = PLAYSTYLES[playstyle][DEFENSE]
    sp_atk = PLAYSTYLES[playstyle][SPATTACK]
    sp_def = PLAYSTYLES[playstyle][SPDEFENSE]
    spd = PLAYSTYLES[playstyle][SPEED]
    hp = PLAYSTYLES[playstyle][HP]
   
    # The '4' can be changed depending on how we want to scale down the social factor.
    # Will probably make this more sophisticated
    social_weight = pkmn_weights[pkmn.name]/4
    
    score = (pkmn.attack * atk + pkmn.defense * defs + pkmn.sp_attack * sp_atk + pkmn.sp_defense * sp_def +
             pkmn.hp * hpp + pkmn.speed * spd + social_weight)
    return score
        
        
    

def findCounters(current_team, uncountered_opponent_team, want_legendary, generations, playstyle, minimum_capture_rate, pkmn_dict):
    """ Updates the current_team with pokemon to counter each of the Pokemon in the
    uncountered_opponent_team.
    
    Parameters:
    current_team: List of the names of the Pokemon in the current team [list of strings]
    uncountered_opponent_team: List of the names of the Pokemon that need to be countered [list of strings]
    want_legendary: Whether legendary pokemon should be included [bool]
    generations: Generations that the pokemon retrieved should be from [list of ints]
    playstyle: One of "balanced", "defensive" or "glass cannon"
    minimum_capture_rate: The minimum capture rate wanted [float]
    pkmn_dict: Dictionary of all Pokemon instances
    
    Note: if no opponent team was specified, then uncountered_opponent_team should be empty.
    """
    all_pokemon = pkmn_dict
    # Filter the list of all Pokemon to satisfy the given filters
    # all_pokemon dictionary should be in app.py
    filtered_pkmn = []
    for pkmn in all_pokemon:
        if (pkmn not in current_team and pkmn.gen in generations and
            pkmn.is_legendary == want_legendary and pkmn.capture_rate >= minimum_capture_rate):
                filtered_pkmn.append(all_pokemon(pkmn))
                    
    for target_name in uncountered_opponent_team:
        
        if len(current_team < 6):
            
            # Get the pokemon instance of this Pokemon name
        
            target = all_pokemon[target_name]
            weaknesses = target.weaknesses
            
            # Retrieve Pokemon that expose these weaknesses and satisfy the filters
            counters = []
            for pkmn_inst in filtered_pkmn:
                if (all_pokemon[pkmn].type1 in weaknesses or all_pokemon[pkmn].type2 in weaknesses):
                    counters.append(pkmn_inst)
                    
            # Need to rank the possible counters in order to retrieve the best one.
            # Will probably use lambda function in conjunction with the generateScore function.
            
            ranked_counters = sorted(counters, key = lambda pk : generateScore(pk), reverse = True)
            
            # Add best counter to current team
            current_team.append(ranked_counters[0].name)
        

    
        
        