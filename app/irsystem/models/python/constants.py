#Returning/Incoming Dictionary keys
MOVES = "moves"
NATURE = "nature"
ITEM = "item"
ABILITY = "ability"

#Branching factors
BRANCH1 = 100
BRANCH2 = 25
BRANCH3 = 10
BRANCH4 = 8
BRANCH5 = 5
BRANCH6 = 4

#Total Number of Pokemon
TOTALPOKEMON= 808

#Empty pokemon, serves as an empty pokemon or empty spot in the team.
EMPTY = "empty"

#Number losing teams to consider on similarity, and number of teams to return to front end.
NUMLOSINGTEAMS = 3
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
    UBER,
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

PATHTOMOVES = "/dataset/PokemonToMovesetsAndNaturesAndItems.json"

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
WEAKNESS3 = .1
WEAKNESS4 = .2
WEAKNESS5 = .3
WEAKNESS6 = .4

#Base Stats
ATTACK = "attack"
DEFENSE = "defense"
SPDEFENSE = "spdefense"
SPATTACK = "spattack"
SPEED = "speed"
HEALTH = "health"

#Playstyles
BALANCED  = "balanced"
GLASS_CANNON = "glass-cannon"
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
        ATTACK : .8,
        DEFENSE : 1.2,
        SPDEFENSE : 1.2,
        SPATTACK : .8,
        SPEED : .8,
        HEALTH : 1.2,
    },
    GLASS_CANNON : {
        ATTACK : 1.2,
        DEFENSE : .8,
        SPDEFENSE : .8,
        SPATTACK : 1.2,
        SPEED : 1.2,
        HEALTH : .8
    }

}
)
