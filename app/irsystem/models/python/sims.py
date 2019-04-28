from . import fillTeam
from . import findCounters
from . import checkCounters
from . import sims as team
from . import movesetsAndFormat
from . import pokemon
from .constants import *

import os
import json
import numpy as np
import time
import random

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
        print(e)
        return None

def teamToArray(team, pokedex):
    arr = np.zeros(TOTALPOKEMON)

    for name in team:
        if name == EMPTY:
            arr[0] += 1
        else:
            arr[pokedex[name].pokedex_num]+=1
    return arr

def loadSims():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path + PATHTOSIMSCORES, "r+") as f:
        data = json.loads(f.readline())

    for k in data:
        data[k] = np.array(data[k])

    return data

def determineWinner(entry):
    if entry["winner"] == "p1":
        winner = entry["p1_team"]
        loser = entry["p2_team"]
    else:
        winner = entry["p2_team"]
        loser = entry["p1_team"]
    
    return winner, loser


def getSimPokemon(pokemon,sims):
    if pokemon in sims:
        return sims[pokemon]

    for k in sims:
        return np.zeros(len(sims[k]))
    


def scoreTeams(curTeams, oppTeam, pokedex, league, minDistWanted):
    """
    Returns NUMTEAMSRETURN number of teams from curTeams as 'top' teams based on social data, along with a list of their scores.

    curTeams - list of pokemon teams to consider
    oppTeam - team of pokemon representing opponent team
    pokedex - dictionary with pokemon names as keys to pokemon instances as values
    league - one of the 11 supported league types, telling us which information to look for similar opponents in
    minDistWanted - an integer denoting how far away we want the team to be in pokemon to be considered valid
    """
    battleData = loadBattleData(league)
    similarities = loadSims()
  
    #If not given an opponent team then simply randomly choose losers from the dataset to compare to.
    if len(oppTeam) == 0:
        picks = set([])
        while (len(picks) < NUMLOSINGTEAMS and (not len(picks) == len(battleData))):
            picks.add(random.randint(0,len(battleData)-1))

        losers = []
        loserDict = {}
        for i in picks:
            entry = battleData[i]
            winner,loser = determineWinner(entry)
            print("winner - "+str(winner))
            loserDict[str(loser)] = [teamToArray(winner,pokedex)]
            losers.append( (loser,0) )

    #Given opponent team then find similar teams
    else:
        oppTeam = [getSimPokemon(opp,similarities) for opp in oppTeam]

        #create dictionary from losers team to the team that beat them.
        loserDict = {}
        sims = []
        for d in battleData:
            winner, loser = determineWinner(d)

            wTeam = teamToArray(winner,pokedex)
            lTeam = np.array(teamToArray(loser, pokedex))

            score = 0
            for oppNp in oppTeam:
                score+= np.amax(lTeam*oppNp)       

            if str(loser) in loserDict:
                loserDict[str(loser)].append(wTeam)
            else:
                #new to dictonary
                loserDict[str(loser)] = [wTeam]

                sims.append((loser, score))


        sims = sorted(sims, key = lambda x : x[1], reverse = True)

        cutoff = min(len(sims),NUMLOSINGTEAMS)
        losers = sims[:cutoff]

    #Gather winners to losing teams
    winnersComp = []
    for loser,_ in losers:
        for winner in loserDict[str(loser)]:
            winnersComp.append(winner)
    
    topScore = len(winnersComp)*6 #pkmn team size

    results = []
    inverted_idx = {}

    existsSet = []

    #Creates inverted index for teams, while simoultaneously weeding out any teams that are exactly similar.
    for i in range(len(curTeams)):
        team = curTeams[i]
        results.append((team,0))
        sTeam = set(team)
        if not (sTeam in existsSet):
            existsSet.append(sTeam)
            for pkm in team:
                if pkm != EMPTY:
                    if pkm in inverted_idx:
                        inverted_idx[pkm].append(i)
                    else:
                        inverted_idx[pkm] = [i]
        
    #Giving the similiarity scores to the winners based off of the inverted index.
    for pkm in inverted_idx:
        for winner in winnersComp:
            wArr = np.array(winner)
            #tArr = getSimPokemon(pkm,similarities)
            tArr = similarities[pkm]
            
            vals = wArr * tArr

            score = np.amax(vals)

            for i in inverted_idx[pkm]:
                results[i] = (results[i][0],results[i][1]+(score/topScore))

    results = sorted(results, key = lambda x : x[1], reverse = True)

    if len(results) < NUMTEAMSRETURN:
        return [result[0] for result in results], [result[1] for result in results]
    
    else:
        firstResult, firstScore = results[0]
        returnTeams = [firstResult]
        teamScores = [round(firstScore*100,1)]
        returnSets = [set(firstResult)]
        
        i = 1

        #Loops through results and adds teams with the proper edit distance away.
        while(len(returnTeams) < NUMTEAMSRETURN and minDistWanted > 0):
            teamToConsider,teamToConsiderScore = results[i]
            
            considerSet = set(teamToConsider)
            add = True
            ##checks the edit distance of teams is above wanted
            for team in returnSets:
                if len(team.union(considerSet)) < len(team)+minDistWanted:
                    add = False

            ##If indeed above wanted levels then add
            if add:
                returnTeams.append(teamToConsider)
                returnSets.append(considerSet)
                teamScores.append(round(teamToConsiderScore*100,1))
            
            i+=1

            if i >= len(results):
                i = 1
                minDistWanted -= 1 

        return returnTeams,teamScores

    
