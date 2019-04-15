from .constants import *
from . import pokemon

def rankPokemon(pObj, playstyle, currentTeamWeaknesses):
    """
    returns a numerical ranking of the pokemon based off of its base stats

    pObj - Pokemon Object - pokemon object of the pokemon to rank
    playstyle - String - string from constants that denotes he playstyle the player has chosen
    currentTeamWeaknesses - dict<pType,numWeak> - pType type of pokemon and the corresponding
        number of pokemon weak to that specific type
    socialWeight - int - the social weight to consider when ranking the pokemon
    """
    #determine weakness multipliers for the pokemon
    weaknessMod = 1
    for weakness in pObj.weaknesses:
        if currentTeamWeaknesses[weakness] + 1 == 3:
            weaknessMod  -= WEAKNESS3

        if currentTeamWeaknesses[weakness] + 1 == 4:
            weaknessMod  -= WEAKNESS4

        if currentTeamWeaknesses[weakness] + 1 == 5:
            weaknessMod  -= WEAKNESS5

        if currentTeamWeaknesses[weakness] + 1 == 6:
            weaknessMod  -= WEAKNESS6


    return weaknessMod * (
        pObj.attack * PLAYSTYLES[playstyle][ATTACK] +
        pObj.defense * PLAYSTYLES[playstyle][DEFENSE] +
        pObj.sp_attack * PLAYSTYLES[playstyle][SPATTACK] +
        pObj.sp_defense * PLAYSTYLES[playstyle][SPDEFENSE] +
        pObj.speed * PLAYSTYLES[playstyle][SPEED] +
        pObj.hp * PLAYSTYLES[playstyle][HEALTH]
    )


def fillRestOfTeam(currentTeams, wantLegendary, generations, playstyle, minCaptureRate, pokemonDictionary, branchFactor,league):
    """
    Updates and returns the currentTeam variable to fill out to six pokemon

    Note -- should we simply ignore the other teams and go for the best balanced?

    currentTeams - List<List<string>> - list of list of pokemon names that are currently on the team
    wantLegendary - Bool - True if allowed to pick legendary pokemon, false if not
    generations - List<ints> - List of integers representing the generations allowed to be chosen from
    playstyle - String - string from constants that denotes he playstyle the player has chosen
    minCaptureRate - float - minimum capture rate that the player willing to endure
    pokemonDictionary - dict<pName,pObj> - where pName is the string name of the pokemon and the pObj is the pokemone object associated with that pokemon
    branchFactor - int - number of different pokemon we should put when building variations.
    league - one of the defined constants for league ranks
    """

    pDict = pokemonDictionary

    finishedTeams = []

    while(len(currentTeams) > 0):
        #if the team is already full then simply return
        team = currentTeams.pop(0)

        if len(team) >= 6:
            finishedTeams.append(team)
        else:
            teamWeaknesses = {}
            #initialize for the types.
            for pTypes in PTYPES:
                teamWeaknesses[pTypes] = 0

            for pokemon in team:
                #Build the team weakness.
                pObj = pDict[pokemon]
                for pType in pObj.weaknesses:
                        teamWeaknesses[pType] += 1

            toRank = []
            for pKey in pDict:
                pObj = pDict[pKey]
                #if not in blacklist or on current team.
                if (pObj.name in team):
                    pass
                elif pObj.is_legendary and (not wantLegendary):
                    pass
                elif not pObj.gen in generations:
                    pass
                elif pObj.capture_rate < minCaptureRate:
                    pass
                elif not pObj.tier in LEAGUERANKS[LEAGUERANKS.index(league):]:
                    pass
                else:
                    toRank.append(pObj)

            #if due to constraints, there is no pokemon that can go in then
            #fill the team with emptys and consider done.
            if len(toRank) == 0:
                for x in range(6-len(team)):
                    team.append(EMPTY)
                finishedTeams.append(team)

            ## rankings - List<strin,score>
            rankings = []
            for pObj in toRank:
                rankings.append((pObj.name,rankPokemon(pObj, playstyle, teamWeaknesses)))

            rankings = sorted(rankings, key = lambda x : x[1], reverse = True)

            #compensate for not having enough pokemon to meet branching factor
            bFactor = min(len(rankings),branchFactor)

            for pName,_ in rankings[:bFactor]:
                tmp = team[:]
                tmp.append(pName)
                currentTeams.append(tmp)

    return finishedTeams

if __name__ == '__main__':
    fillRestOfTeam([['Lucario','Arcanine']], False, [1,2,3,4,5,6], BALANCED, 0, [], pokemon.generate_instances(), 5)