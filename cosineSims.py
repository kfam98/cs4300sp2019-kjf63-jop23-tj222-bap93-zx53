from constants import *
import pokemon
import json
import numpy as np

count = 0

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

def teamToArray(team, pokedex):
    arr = np.zeros(TOTALPOKEMON)
    for name in team:
        if name == EMPTY:
            arr[0] += 1
        else:
            try:
                arr[pokedex[name].pokedex_num]+=1  
            except:
                global count
                count+=1
                print("I hate Jesse: "+str(count))
    return arr


def scoreTeams(curTeams, oppTeam, pokedex, level):
    battleData = loadBattleData(level)

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
    print("cutoff to be returned is: "+str(cutoff))
    results = results[:cutoff]

    return [result[0] for result in results]