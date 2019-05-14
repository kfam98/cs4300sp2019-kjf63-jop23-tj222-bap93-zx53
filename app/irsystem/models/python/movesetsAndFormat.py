from . import pokemon
import json
from .constants import *
import os

def loadMovesets():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path+PATHTOMOVES, "r+") as f:
        return json.loads(f.readline())


def loadWinPercents(league):
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path + PATHTOWINPERCENTS, "r+") as f:
        data = json.loads(f.readline())

    if league in data:
        return data[league]

    return None


def loadHtmlToIds():
    path = os.path.dirname(os.path.realpath(__file__))
    
    with open(path+PATHTOREPLAYSOCKETS, "r+") as f:
        return json.loads(f.readline())

def fillAndFormat(teams, currentTeamData, tScores, league, winnerHtmls):
    """
    Return properly formatted teams to push back to front end

    teams - List of teams to fill the movesets and natures for
    currentTeamData - dictionary that is the format of the initial input,
        pokemon key to dictionary with moves and nature for that pokemon
    tScores - scores of the individual teams
    league - one of the 11 supported league types, telling us which information to look for similar opponents in
    winnerHtmls - list of the file names associated with the winning teams.
    """

    movesDict = loadMovesets()

    winPercents = loadWinPercents(league)

    htmlsToIds = loadHtmlToIds()

    ids = []
    for w in winnerHtmls:
        ids.append(htmlsToIds[w])

    toRet = []

    for i in range(len(teams)):
        team = teams[i]
        sTeam = set(team)
        if len(sTeam) == 1 and EMPTY in sTeam:
            toRet.append([])
            continue
        teamData = []
        teamData.append(tScores[i])
        teamData.append(ids)
        for pokeman in team:
            if not pokeman == EMPTY:
                form = {}
                #initialize pokemans entry
                form[pokeman] = {}
                form[pokeman][MOVES] = []
                form[pokeman][NATURE] = None
                form[pokeman][ABILITY] = None
                form[pokeman][ITEM] = None

                if pokeman in currentTeamData:
                    #add additional moves
                    for move in currentTeamData[pokeman][MOVES]:
                        form[pokeman][MOVES].append(move)
                    form[pokeman][NATURE] = currentTeamData[pokeman][NATURE]

                if len(movesDict[pokeman]) > 0:
                    d = movesDict[pokeman][0]
                    for move in d[MOVES]:
                        if len(form[pokeman][MOVES]) < 4 and (not move in form[pokeman][MOVES]):
                            form[pokeman][MOVES].append(move)

                    if form[pokeman][NATURE] == None:
                        form[pokeman][NATURE] = d[NATURE]
                    
                    if form[pokeman][ABILITY] == None:
                        form[pokeman][ABILITY] = d[ABILITY]
                    
                    if form[pokeman][ITEM] == None:
                        form[pokeman][ITEM] = d[ITEM]
                    
                if pokeman in winPercents:
                    form[pokeman][WINPERCENT] = round(100*((winPercents[pokeman][WINS] - (.5*winPercents[pokeman][TOTALMATCHES])) / winPercents[pokeman][TOTALMATCHES]),1)

                    if winPercents[pokeman][TOTALMATCHES] < LOWCONFIDENCEBOUND:
                        form[pokeman][CONFIDENCELEVEL] = OKAY
                    elif winPercents[pokeman][TOTALMATCHES] < HIGHCONFIDENCEBOUND:
                        form[pokeman][CONFIDENCELEVEL] = GOOD
                    else:
                        form[pokeman][CONFIDENCELEVEL] = GOOD
                else:
                    form[pokeman][WINPERCENT] = None
                    form[pokeman][CONFIDENCELEVEL] = None

                teamData.append(form.copy())

        toRet.append(teamData.copy())

    #If the team is empty 
    if len(toRet) < NUMTEAMSRETURN:
        for x in range((NUMTEAMSRETURN - len(toRet))):
            toRet.append([])

    return toRet