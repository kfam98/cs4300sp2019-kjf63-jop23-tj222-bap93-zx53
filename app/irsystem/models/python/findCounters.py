from .constants import *
from . import pokemon
pokedex = pokemon.generate_instances()

# At this stage, we should know which of the opponent's Pokemon are not countered
# by any of the current team

# Want to find pokemon to add to current team that counter the rest of the opponent's team


def generateScore(pkmn, playstyle):
    """ Returns a score for the pkmn to be used for ranking, based on the playstyle

    Parameters:
    pkmn: The Pokemon instance [pokemon.Pokemon instance]
    playstyle: One of "balanced", "defensive" or "glass-cannon"
    """
    atk = PLAYSTYLES[playstyle][ATTACK]
    defs = PLAYSTYLES[playstyle][DEFENSE]
    sp_atk = PLAYSTYLES[playstyle][SPATTACK]
    sp_def = PLAYSTYLES[playstyle][SPDEFENSE]
    spd = PLAYSTYLES[playstyle][SPEED]
    hp = PLAYSTYLES[playstyle][HEALTH]


    score = (pkmn.attack * atk +
            pkmn.defense * defs +
            pkmn.sp_attack * sp_atk +
            pkmn.sp_defense * sp_def +
            pkmn.hp * hp +
            pkmn.speed * spd)
    return score




def findCounters(current_team, uncountered_opponent_team, want_legendary, generations, playstyle, minimum_capture_rate, pkmn_dict, branch_factor, tier):
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
    branch_factor: the branching factor [int]
    tier: The maximum tier the pokemon found should be

    Note: if no opponent team was specified, then uncountered_opponent_team should be empty.
    """
    all_pokemon = pkmn_dict
    # Filter the list of all Pokemon to satisfy the given filters

    filtered_pkmn = []
    for pkmn in all_pokemon:
        if all_pokemon[pkmn].name == "Pheromosa":
            print("Cap rate is " + str(all_pokemon[pkmn].capture_rate))
        if (pkmn not in current_team and all_pokemon[pkmn].gen in generations and
            all_pokemon[pkmn].is_legendary <= want_legendary and all_pokemon[pkmn].capture_rate >= minimum_capture_rate):

            current_tier_index = LEAGUERANKS.index(tier)
            poke_tier_index = LEAGUERANKS.index(all_pokemon[pkmn].tier)

            if poke_tier_index >= current_tier_index:
                filtered_pkmn.append(all_pokemon[pkmn])
                
    possible_teams = [current_team]
    for target_name in uncountered_opponent_team:

        if len(possible_teams[0]) < 6:
            # Get the pokemon instance of this Pokemon name

            target = all_pokemon[target_name]
            weaknesses = target.weaknesses

            # Retrieve Pokemon that expose these weaknesses and satisfy the filters

            counters = []
            for pkmn_inst in filtered_pkmn:
                if (pkmn_inst.type1 in weaknesses or pkmn_inst.type2 in weaknesses):
                    counters.append(pkmn_inst)

            # Need to rank the possible counters in order to retrieve the best one.

            ranked_counters = sorted(counters, key = lambda pk : generateScore(pk, playstyle), reverse = True)
            cutoff = min(branch_factor,len(counters))
            best_counters = ranked_counters[:cutoff]
            # Generate possible teams with best counters

            new_teams = []
            for team in possible_teams:
                for counter in best_counters:
                    
                    if counter.name not in team:
                        new_teams.append(team + [counter.name])

            possible_teams = new_teams


    return possible_teams


if __name__ == '__main__':
    print(findCounters(['Charizard'], ['Pikachu', 'Blastoise'], False, [1,2,3,4,5,6,7], BALANCED, 0, pokedex, BRANCH1, OU))
