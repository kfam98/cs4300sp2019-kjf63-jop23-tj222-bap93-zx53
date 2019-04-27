var naturesLst = [
  {'text': 'Naughty', 'id': 17},
  {'text': 'Impish', 'id': 12},
  {'text': 'Gentle', 'id': 9},
  {'text': 'Mild', 'id': 8},
  {'text': 'Brave', 'id': 21},
  {'text': 'Adamant', 'id': 11},
  {'text': 'Rash', 'id': 15},
  {'text': 'Jolly', 'id': 16},
  {'text': 'Calm', 'id': 4},
  {'text': 'Quirky', 'id': 19},
  {'text': 'Relaxed', 'id': 22},
  {'text': 'Lonely', 'id': 6},
  {'text': 'Bold', 'id': 2},
  {'text': 'Naive', 'id': 20},
  {'text': 'Bashful', 'id': 13},
  {'text': 'Modest', 'id': 3},
  {'text': 'Lax', 'id': 18},
  {'text': 'Docile', 'id': 7},
  {'text': 'Sassy', 'id': 24},
  {'text': 'Careful', 'id': 14},
  {'text': 'Timid', 'id': 5},
  {'text': 'Hardy', 'id': 1},
  {'text': 'Hasty', 'id': 10},
  {'text': 'Quiet', 'id': 23},
  {'text': 'Serious', 'id': 25}
];

var leaguesLst = [
  {'text': 'UBER', 'id': 1},
  {'text': 'OU', 'id': 2},
  {'text': 'UU', 'id': 3},
  {'text': 'RU', 'id': 4},
  {'text': 'NU', 'id': 5},
  {'text': 'PU', 'id': 6},
  {'text': 'LC', 'id': 7},
  {'text': 'NFE', 'id': 8},
];

var romanToNumbers = {
  "I":1,
  "II":2,
  "III":3,
  "IV":4,
  "V":5,
  "VI": 6,
  "VII": 7

};

var pstyleLst = [
  {id: 1, text:"Offensive"},
  {id: 2, text:"Balanced"},
  {id: 3, text:"Defensive"}
];

var genLst = [
  {id: 1, text:"I"},
  {id: 2, text:"II"},
  {id: 3, text:"III"},
  {id: 4, text:"IV"},
  {id: 5, text:"V"},
  {id: 6, text:"VI"},
  {id: 7, text:"VII"}
];

var types= {
  'normal': '#A8A77A',
  'fire': '#EE8130',
  'water':'#6390F0',
  'electric': '#F7D02c',
  'grass': '#7AC74C',
  'ice':  '#96D9D6',
  'fighting': '#C22E28',
  'poison':  '#A33EA1',
  'ground':  '#E2BF65',
  'flying':  '#A98FF3',
  'psychic':  '#F95587',
  'bug':  '#A6B91A',
  'rock':  '#B6A136',
  'ghost':  '#735797',
  'dragon':  '#6F35FC',
  'dark':  '#705746',
  'steel':  '#B7B7CE',
  'fairy':  '#D685AD',
  '':'',
}

var natureStats = {
    "Hardy" : {
        "increase": "Attack",
        "decrease": "Attack"
    },
    "Lonely" : {
        "increase": "Attack",
        "decrease": "Defense"
    },
    "Brave" : {
        "increase": "Attack",
        "decrease": "Speed"
    },
    "Adamant" : {
        "increase": "Attack",
        "decrease": "Special Attack"
    },
    "Naughty" : {
        "increase": "Attack",
        "decrease": "Special Defense"
    },
    "Bold" : {
        "increase": "Defense",
        "decrease": "Attack"
    },
    "Docile" : {
        "increase": "Defense",
        "decrease": "Defense"
    },
    "Relaxed" : {
        "increase": "Defense",
        "decrease": "Speed"
    },
    "Impish" : {
        "increase": "Defense",
        "decrease": "Special Attack"
    },
    "Lax" : {
        "increase": "Defense",
        "decrease": "Special Defense"
    },
    "Timid" : {
        "increase": "Speed",
        "decrease": "Attack"
    },
    "Hasty" : {
        "increase": "Speed",
        "decrease": "Defense"
    },
    "Serious" : {
        "increase": "Speed",
        "decrease": "Speed"
    },
    "Jolly" : {
        "increase": "Speed",
        "decrease": "Special Attack"
    },
    "Naive" : {
        "increase": "Speed",
        "decrease": "Special Defense"
    },
    "Modest" : {
        "increase": "Special Attack",
        "decrease": "Attack"
    },
    "Mild" : {
        "increase": "Special Attack",
        "decrease": "Defense"
    },
    "Quiet" : {
        "increase": "Special Attack",
        "decrease": "Speed"
    },
    "Bashful" : {
        "increase": "Special Attack",
        "decrease": "Special Attack"
    },
    "Rash" : {
        "increase": "Special Attack",
        "decrease": "Special Defense"
    },
    "Calm" : {
        "increase": "Special Defense",
        "decrease": "Attack"
    },
    "Gentle" : {
        "increase": "Special Defense",
        "decrease": "Defense"
    },
    "Sassy" : {
        "increase": "Special Defense",
        "decrease": "Speed"
    },
    "Careful" : {
        "increase": "Special Defense",
        "decrease": "Special Attack"
    },
    "Quirky" : {
        "increase": "Special Defense",
        "decrease": "Special Defense"
    }
};
