SCORE = "score"

#Returning/Incoming Dictionary keys
MOVES = "moves"
NATURE = "nature"
ITEM = "item"
ABILITY = "ability"
WINPERCENT = "win_percent"
CONFIDENCELEVEL = "confidence_level"
OKAY = "Okay"
GOOD = "Good"
GREAT = "Great"

LOWCONFIDENCEBOUND = 20
HIGHCONFIDENCEBOUND = 100

WINS = "WINS"
TOTALMATCHES = "TOTALMATCHES"

#Branching factors
BRANCH1 = 100
BRANCH2 = 25
BRANCH3 = 10
BRANCH4 = 8
BRANCH5 = 5
BRANCH6 = 4

#Total Number of Pokemon
TOTALPOKEMON= 820

#Empty pokemon, serves as an empty pokemon or empty spot in the team.
EMPTY = "empty"

#Number losing teams to consider on similarity, and number of teams to return to front end.
NUMLOSINGTEAMS = 5
NUMTEAMSRETURN = 5

#Leagues
UBER = "UBER"
OU = "OU"
UUBL = "UUBL"
UU = "UU"
RUBL = "RUBL"
RU = "RU"
NUBL = "NUBL"
NU = "NU"
PUBL = "PUBL"
PU = "PU"
LC = "LC"
NFE = "NFE"

LEAGUERANKS = [
    UBER,
    OU,
    UUBL,
    UU,
    RUBL,
    RU,
    NUBL,
    NU,
    PUBL,
    PU,
    LC,
    NFE
]

RANKSTOWINLOSEFILES = [
    "/dataset/replays_html/rp_file_ou.json",
    "/dataset/replays_html/rp_file_ou.json",
    UUBL,
    "/dataset/replays_html/rp_file_uu.json",
    RUBL,
    "/dataset/replays_html/rp_file_ru.json",
    NUBL,
    "/dataset/replays_html/rp_file_nu.json",
    PUBL,
    "/dataset/replays_html/rp_file_pu.json",
    "/dataset/replays_html/rp_file_lc.json",
    "/dataset/replays_html/rp_file_nfe.json"

]

WINHTMLFILES = [
    "/dataset/replays_html/html_ou.json",
    "/dataset/replays_html/html_ou.json",
    UUBL,
    "/dataset/replays_html/html_uu.json",
    RUBL,
    "/dataset/replays_html/html_ru.json",
    NUBL,
    "/dataset/replays_html/html_nu.json",
    PUBL,
    "/dataset/replays_html/html_pu.json",
    "/dataset/replays_html/html_lc.json",
    "/dataset/replays_html/html_nfe.json"
    
]

PATHTOREPLAYSOCKETS = "/dataset/replays_html/replay_ids.json"

PATHTOMOVES = "/dataset/PokemonToMovesetsAndNaturesAndItems.json"
PATHTOSIMSCORES = "/dataset/updatedSims.json"
PATHTOMLWEIGHTS = "/dataset/classWeights.json"
PATHTOWINPERCENTS = "/dataset/pythonwinPercents.json"

#Pokemon Types
BUG = 'bug'
DARK = 'dark'
DRAGON = 'dragon'
ELECTRIC =  'electric'
FAIRY = 'fairy'
FIGHTING = 'fighting'
FIRE = 'fire'
FLYING = 'flying'
GHOST = 'ghost'
GRASS = 'grass'
GROUND = 'ground'
ICE = 'ice'
NORMAL = 'normal'
POISON = 'poison'
PSYCHIC = 'psychic'
ROCK = 'rock'
STEEL = 'steel'
WATER = 'water'

PTYPES = [BUG, DARK, DRAGON, ELECTRIC, FAIRY, FIGHTING, FIRE, FLYING,
         GHOST, GRASS, GROUND, ICE, NORMAL, POISON, PSYCHIC, ROCK,
         STEEL, WATER]

#Weakness Multipliers
WEAKNESS3 = .2
WEAKNESS4 = .4
WEAKNESS5 = .6
WEAKNESS6 = .8

#Base Stats
ATTACK = "attack"
DEFENSE = "defense"
SPDEFENSE = "spdefense"
SPATTACK = "spattack"
SPEED = "speed"
HEALTH = "health"

#Playstyles
BALANCED  = "balanced"
GLASS_CANNON = "offensive"
DEFENSIVE = "defensive"

#playstyles dictionary, used to find weights
PLAYSTYLES = (
{

    BALANCED : {
        ATTACK : 1,
        DEFENSE : 1,
        SPDEFENSE : 1,
        SPATTACK : 1,
        SPEED : 1,
        HEALTH : 1,
    },
    DEFENSIVE : {
        ATTACK : .1,
        DEFENSE : 1.9,
        SPDEFENSE : 1.9,
        SPATTACK : .1,
        SPEED : .1,
        HEALTH : 1.9,
    },
    GLASS_CANNON : {
        ATTACK : 1.9,
        DEFENSE : .1,
        SPDEFENSE : .1,
        SPATTACK : 1.9,
        SPEED : 1.9,
        HEALTH : .1
    }

}
)
