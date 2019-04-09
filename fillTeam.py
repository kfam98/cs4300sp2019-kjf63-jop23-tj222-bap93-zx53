from constants import * 
import pokemon

def rankPokemon(pObj, playstyle, currentTeamWeaknesses, socialWeight):
    """
    returns a numerical ranking of the pokemon based off of its base stats

    pObj - Pokemon Object - pokemon object of the pokemon to rank
    playstyle - String - string from constants that denotes he playstyle the player has chosen
    currentTeamWeaknesses - dict<pType,numWeak> - pType type of pokemon and the corresponding number of pokemon weak to that specific type 
    socialWeight - int - the social weight to consider when ranking the pokemon
    """
    #determine weakness multipliers for the pokemon
    avg = 0
    for weakness in pObj.weaknesses:
        if currentTeamWeaknesses[weakness] + 1 == 1:
            avg += WEAKNESS1 / len(pObj.weaknesses)

        if currentTeamWeaknesses[weakness] + 1 == 2:
            avg += WEAKNESS2 / len(pObj.weaknesses)

        if currentTeamWeaknesses[weakness] + 1 == 3:
            avg += WEAKNESS3 / len(pObj.weaknesses)

        if currentTeamWeaknesses[weakness] + 1 == 4:
            avg += WEAKNESS4 / len(pObj.weaknesses)

        if currentTeamWeaknesses[weakness] + 1 == 5:
            avg += WEAKNESS5 / len(pObj.weaknesses)

        if currentTeamWeaknesses[weakness] + 1 == 6:
            avg += WEAKNESS6 / len(pObj.weaknesses)

    
    return avg * (
        pObj.attack * PLAYSTYLES[playstyle][ATTACK] + 
        pObj.defense * PLAYSTYLES[playstyle][DEFENSE] + 
        pObj.sp_attack * PLAYSTYLES[playstyle][SPATTACK] + 
        pObj.sp_defense * PLAYSTYLES[playstyle][SPDEFENSE] + 
        pObj.speed * PLAYSTYLES[playstyle][SPEED] + 
        pObj.hp * PLAYSTYLES[playstyle][HEALTH] +
        socialWeight
    )


def fillRestOfTeam(currentTeam, wantLegendary, generations, playstyle, minCaptureRate, blacklist, pokemonDictionary, socialWeights):
    """
    Updates and returns the currentTeam variable to fill out to six pokemon

    Note -- should we simply ignore the other teams and go for the best balanced?

    currentTeam - List<string> - list of pokemon names that are currently on the team
    wantLegendary - Bool - True if allowed to pick legendary pokemon, false if not
    generations - List<ints> - List of integers representing the generations allowed to be chosen from
    playstyle - String - string from constants that denotes he playstyle the player has chosen
    minCaptureRate - float - minimum capture rate that the player willing to endure
    blacklist - List<string> - string of pokemon names not allowed to be on the team
    pokemonDictionary - dict<pName,pObj> - where pName is the string name of the pokemon and the pObj is the pokemone object associated with that pokemon
    pokemonDictionary - dict<pName,w> - where pName is the string name of the pokemon and the corresponding social weight as an int
    """

    pDict = pokemonDictionary

    #if the team is already full then simply return
    if len(currentTeam) >= 6:
        return
    
    while (len(currentTeam) < 6):

        teamWeaknesses = {}
        for pTypes in PTYPES:
            teamWeaknesses[pTypes] = 0

        for pokemon in currentTeam:
            #Build the team weakness.
            pObj = pDict[pokemon]
            for pType in pObj.weaknesses:
                    teamWeaknesses[pType] += 1
        
        ## rankings - List<strin,score>
        rankings = []
        for pObj in pDict:
            #if not in blacklist or on current team.
            if (pObj.name in currentTeam) or (pObj.name in blacklist):
                pass
            elif pObj.legendary and (not wantLegendary):
                pass
            elif not pObj.gen in generations:
                pass
            elif pObj.capture_rate < minCaptureRate:
                pass
            else:
                rankings.append(pObj.name,rankPokemon(pObj, playstyle, teamWeaknesses, socialWeights[pObj.name]))

        rankings = sorted(rankings, lambda x: x[1], reverse = True)

        currentTeam += rankings[0][0]
    
    return currentTeam