import pokemon 
from constants import * 

def getUserMoves(input): 
    """ 
    Returns a list of all moves entered for Pokemon on user team. 

    Parameters: 
        input: Dictionary of input information for user Pokemon. Here, I assume
                that the keys are Pokemon names, mapped to dictionaries that 
                will contain a key named "moves" that maps to a list of 
                strings identifying all the moves for that Pokemon. 
    """
    moves = {}

    for (key, value) in input: 
        moves[key] = value["moves"]

    return moves


def checkCounters(user_team, user_moves, opponent_team, all_pokemon, mvtypes): 
    """ 
    Checks if any of the Pokemon on the user input team serve as counters to any
    of the Pokemon on the opponent team. A "counter" is defined as a Pokemon
    who either
        1) is of the type strong against the opponent Pokemon type or
        2) knows moves of the type strong against the opponent Pokemon type. 
    
    Parameters: 
        user_team: List of string names of each Pokemon on user team
        user_moves: List of all moves entered for Pokemon on user team
        opponent_team: List of string names of each Pokemon on opponent team
        all_pokemon: Dictionary of all instances of Pokemon objects
        mvtypes: Dictionary of move names and their corresponding types

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


    for i in range(len(opponent_team)): 
        opp = opponent_team[i]
        # get opponent pokemon weaknesses 
        opp_weak = opponents[i].weaknesses

        # iterate through all of user's pokemon
        for j in range(len(user_team)): 

            # no need to go through any of this if opponent already countered
            if opp in uncountered: 

                # check if any user pokemon move types counter opponent type 
                moves = user_moves[team[j].name]
                mvtypes = [mvtypes[mv] for mv in moves]
                movecounter = not set(opp_weak).isdisjoint(set(mvtypes))

                # if four moves entered, only check if any counter 
                if len(moves) == 4:
                    if movecounter: 
                        uncountered.remove(opp)

                # else check if either type or move types counter     
                else: 
                    pkmn_type = team[j].type1
                    typecounter = pkmn_type in opp_weak


                    if typecounter or movecounter: 
                        uncountered.remove(opp)
    
    return uncountered 

                    







    

