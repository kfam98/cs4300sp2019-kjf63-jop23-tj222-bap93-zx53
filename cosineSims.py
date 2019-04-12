from constants import *
import pokemon
import json
import numpy as np

def loadBattleData(level):
    """
    Returns loaded data associated with the league levels, or none if associated with no league data.

    level - one of the 11 defined levels 


    """
    fString = None
    if level == OU:
        fString = "./app/data/replays_html/rp_file.json"

    if not fString == None:
        with open(fString, "r+") as f:
            battleData = json.loads(f.readline())

        return battleData
    
    return None


def scoreTeams(curTeams, oppTeam, level):
    battleData = loadBattleData(level)

    if len(oppTeam) < 6:
        for x in range(6-len(oppTeam)):
            oppTeam.append(EMPTY)
    
    oppTeam = np.array(oppTeam)

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
            loserDict[str(loser)].append(winner)
        else:
            #new to dictonary
            loserDict[str(loser)] = [winner]

            #Fix dot product of strings -- later problem
            sims.append((loser, np.dot(oppTeam,np.array(loser)) ))

    
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
        t = np.array(team)
        score = 0
        for winner in winnersComp:
            w = np.array(w)
            score+= np.dot(t,w)
        results.append((team,score))

    results = sorted(results, key = lambda x : x[1], reverse = True)

    cutoff = min(len(results),NUMTEAMSRETURN)
    results[:cutoff]

    return [result[0] for result in results]


