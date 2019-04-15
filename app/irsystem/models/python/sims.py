from .constants import *
from . import pokemon
import json
import numpy as np
import os

count = 0

def loadBattleData(league):
    """
    Returns loaded data associated with the league levels, or none if associated with no league data.

    league - one of the 11 supported leagues
    """
    path = os.path.dirname(os.path.realpath(__file__))
    fString = None
    try:
        idx = LEAGUERANKS.index(league)
        fString = path+RANKSTOWINLOSEFILES[idx]
    except:
        #No file associated with the leauge.
        return None

    try:
        with open(fString, "r+") as f:
            battleData = json.loads(f.readline())
        return battleData
    except Exception as e:
        return None

def teamToArray(team, pokedex):
    arr = np.zeros(TOTALPOKEMON)

    for name in team:
        if name == EMPTY:
            arr[0] += 1
        else:
            arr[pokedex[name].pokedex_num]+=1
    return arr


def scoreTeams(curTeams, oppTeam, pokedex, league):
    """
    Returns NUMTEAMSRETURN number of teams from curTeams as 'top' teams based on social data.

    curTeams - list of pokemon teams to consider
    oppTeam - team of pokemon representing opponent team
    pokedex - dictionary with pokemon names as keys to pokemon instances as values
    league - one of the 11 supported league types, telling us which information to look for similar opponents in
    """
    battleData = loadBattleData(league)

    if battleData == None:
        cutoff = min(len(curTeams),NUMTEAMSRETURN)
        return curTeams[:cutoff]

    if len(oppTeam) < 6:
        for x in range(6-len(oppTeam)):
            oppTeam.append(EMPTY)

    oppTeam = teamToArray(oppTeam, pokedex)

    #create dictionary from losers team to the team that beat them.
    loserDict = {}
    sims = []
    for d in battleData:
        if d["winner"] == "p1":
            winner = d["p1_team"]
            loser = d["p2_team"]
        else:
            winner = d["p2_team"]
            loser = d["p1_team"]

        if str(loser) in loserDict:
            loserDict[str(loser)].append(teamToArray(winner,pokedex))
        else:
            #new to dictonary
            loserDict[str(loser)] = [teamToArray(winner,pokedex)]

            sims.append((loser, np.dot(oppTeam, teamToArray(loser,pokedex)) ))


    sims = sorted(sims, key = lambda x : x[1], reverse = True)

    cutoff = min(len(sims),NUMLOSINGTEAMS)
    losers = sims[:cutoff]

    #Gather winners to losing teams
    winnersComp = []
    for loser,_ in losers:
        for winner in loserDict[str(loser)]:
            winnersComp.append(winner)

    results = []
    for team in curTeams:
        t = teamToArray(team,pokedex)
        score = 0
        for winner in winnersComp:
            score+= np.dot(t,winner)
        results.append((team,score))

    results = sorted(results, key = lambda x : x[1], reverse = True)

    cutoff = min(len(results),NUMTEAMSRETURN)
    results = results[:cutoff]

    return [result[0] for result in results]
