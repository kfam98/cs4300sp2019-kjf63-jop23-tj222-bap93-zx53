import pokemon 
from constants import * 

def checkCounters(user_team, user_moves, opponent_team, all_pokemon, moves): 
    """ 
    Checks if any of the Pokemon on the user input team serve as counters to any
    of the Pokemon on the opponent team. A "counter" is defined as a Pokemon
    who either
        1) is of the type strong against the opponent Pokemon type or
        2) knows moves of the type strong against the opponent Pokemon type. 
    
    Parameters: 
        user_team: List of string names of each Pokemon on user team
        user_moves: Dictionary of lists of string moves of each user Pokemon
        opponent_team: List of string names of each Pokemon on opponent team
        all_pokemon: Dictionary of all instances of Pokemon objects
        moves: Dictionary of move names and their corresponding types

    Returns: 
        List of string names of uncountered Pokemon on opponent team. If all
        opponent Pokemon are countered, or if opponent_team is an empty list,
        returns an empty list. 
    """
    if opponent_team == []: 
        return [] 

    team = [all_pokemon[entry] for entry in user_team]

    opponents = [all_pokemon[entry] for entry in opponent_team]

    uncountered = opponent_team.copy()

    for opp in opponent_team: 
        # get opponent pokemon weaknesses 
        opp_weak = opponents[opp].weaknesses

        # iterate through all of user's pokemon
        for pkmn in user_team: 

            # no need to go through any of this if opponent already countered
            if opp not in uncountered: 

                # get user pokemon type and check if counters opponent type
                pkmn_type = team[pkmn].type1
                typecounter = pkmn_type in opp_weak

                # check if any user pokemon move types counter opponent type 
                mvtypes = [moves[mv] for mv in user_moves]
                movecounter = not set(opp_weak).isdisjoint(set(mvtypes))

                # if both pokemon type and any move types counter opponent, 
                # opponent is removed from uncountered list 
                if typecounter and movecounter: 
                    uncountered.remove(opp)
    
    return uncountered 

                    







    

