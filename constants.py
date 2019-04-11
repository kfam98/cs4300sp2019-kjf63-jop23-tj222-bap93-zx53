#Returning/Incoming Dictionary keys
MOVES = "moves"
NATURE = "nature"

#Branching factors
BRANCH1 = 100
BRANCH2 = 50
BRANCH3 = 25
BRANCH4 = 12
BRANCH5 = 2#6
BRANCH6 = 3


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