from . import fillTeam
from . import findCounters
from . import checkCounters
from . import sims as team
from . import movesetsAndFormat
from . import pokemon
from .constants import *

import os
import math

##Note - check for extremes like stupid high minimum capture rate or no gens allowed.

def generateResults(myTeam,oppTeam,allowLegends,gens,pStyle,minCapRate, league = OU,pokedex = None,pokeMoves = None):
    """
    Return list of dictionaries, where each dictionary is a proposed team.

    myTeam - dictionary with each key being the pokemon's name.
    oppTeam - dictionary with each key being the pokemon's name, but for opposing team.
    allowLegends - True if allowed to choose from legendaries.
    gens - list of integers showing the allowed generations allowed to choose from.
    pStyle - one of the three playstyles
    minCapRate - float representing the lowest caputre rate the person does not want.

    league - string representing which is the highest league we allow

    """
    

    #Initialization, should only happen once in app but am putting it here now
    if pokedex == None:
        pokedex = pokemon.generate_instances()
    if pokeMoves == None:
        pokeMoves = pokemon.generateMoveData()

    currentTeamNames = []
    currentMoves = {}
    for p in myTeam:
        currentTeamNames.append(p)
        currentMoves[p] = myTeam[p][MOVES]

    oppTeamNames = []
    for p in oppTeam:
        oppTeamNames.append(p)
        
    if len(currentTeamNames) == 6:
        return movesetsAndFormat.fillAndFormat([currentTeamNames],myTeam)

    ##May need to change inputs into the proper backend global vars, a translation

    branchFactor = determineBranchFactor(currentTeamNames)

    if branchFactor == None:
        #avoid algorithm -- call to fill the natures and moves. -- format correctly aft.
        #for now simply dont worry about it
        return myTeam

    desiredDistAway = math.ceil( (6-len(currentTeamNames))/2 )

    uncounteredOpps = checkCounters.checkCounters(
        currentTeamNames,
        currentMoves,
        oppTeamNames,
        pokedex,
        pokeMoves
    )

    possibleTeams = findCounters.findCounters(
        currentTeamNames,
        uncounteredOpps,
        allowLegends,
        gens,
        pStyle,
        minCapRate,
        pokedex,
        branchFactor,
        league
    )

    allPossibleTeams = fillTeam.fillRestOfTeam(
        possibleTeams,
        allowLegends,
        gens,
        pStyle,
        minCapRate,
        pokedex,
        branchFactor,
        league
    )

    topTeams, teamScores = team.scoreTeams(
        allPossibleTeams,
        oppTeamNames,
        pokedex,
        league,
        desiredDistAway
    )

    return movesetsAndFormat.fillAndFormat(
        topTeams,
        myTeam
    )


def determineBranchFactor(curTeam):
    currentMems = len(curTeam)
    if currentMems == 0:
        return BRANCH6
    elif currentMems == 1:
        return BRANCH5
    elif currentMems == 2:
        return BRANCH4
    elif currentMems == 3:
        return BRANCH3
    elif currentMems == 4:
        return BRANCH2
    elif currentMems == 5:
        return BRANCH1
    else:
        return None


if __name__ == '__main__':
    r = generateResults(
        {"Squirtle": {MOVES:[],NATURE:None},"Charmander": {MOVES:[],NATURE:None}} ,
        {"Charmander", "Dragonite"},
        False,
        [1,2,3,4,5,6,7],
        BALANCED,
        0.0
        )

    for team in r:
        print(team)
        print("--------------")
