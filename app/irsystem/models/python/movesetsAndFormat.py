from . import pokemon
import json
from .constants import *
import os
def loadMovesets():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path+PATHTOMOVES, "r+") as f:
        return json.loads(f.readline())


def fillAndFormat(teams, currentTeamData):
    """
    Return properly formatted teams to push back to front end

    teams - List of teams to fill the movesets and natures for
    currentTeamData - dictionary that is the format of the initial input,
        pokemon key to dictionary with moves and nature for that pokemon
    """

    movesDict = loadMovesets()

    toRet = []

    for team in teams:
        form = {}
        for pokeman in team:
            #initialize pokemans entry
            form[pokeman] = {}
            form[pokeman][MOVES] = []
            form[pokeman][NATURE] = None

            if pokeman in currentTeamData:
                #add additional moves
                for move in currentTeamData[pokeman][MOVES]:
                    form[pokeman][MOVES].append(move)
                form[pokeman][NATURE] = currentTeamData[pokeman][NATURE]

            if len(movesDict[pokeman]) > 0:
                d = movesDict[pokeman][0]
                for move in d[MOVES]:
                    if len(form[pokeman][MOVES]) < 4:
                        form[pokeman][MOVES].append(move)

                if form[pokeman][NATURE] == None:
                    form[pokeman][NATURE] = d[NATURE]

        toRet.append(form.copy())

    return toRet
