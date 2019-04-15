from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.python import *
from app.irsystem.models.python.execute import *

import os

# project_name = "SquadUp"
# net_ids = [
#            "Sherry Xie: zx53" ,
#            "Jesse Phillips: jop23",
#            "Kelly Fam: kjf63",
#            "Trevor Jamison: tj222",
#            "Boonakij Palipatana: bap93"
#           ]
#
# @irsystem.route('/', methods=['GET'])
# def search():
# 	query = request.args.get('search')
# 	if not query:
# 		data = []
# 		output_message = ''
# 	else:
# 		output_message = "Your search: " + query
# 		data = range(5)
# 	return render_template('search.html', name=project_name, netids=net_ids, output_message=output_message, data=data)
image_data = {}
path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("irsystem/controllers", "")
with open(path+"static/data/imageslst.json") as json_file:
    image_data = json.load(json_file)

arguments = {}
# arguments = {
#     'myTeam': {'Charmander': {"moves":['ember'], "nature": None}},
#     'oppTeam':{},
#     'gens': [5],
#     'allowLegends': False,
#     'pStyle': 'balanced',
#     'minCapRate': 0.0,
#     # 'league':al
# }


@irsystem.route('/', methods=['GET'])
def search():
    return render_template('index.html')

@irsystem.route('/results', methods=['GET'])
def results():
    # if not arguments:
    #     return render_template('404.html')

    legend = request.args.get('legendary')
    if (legend == 'true'):
        arguments['allowLegends'] = True
    else:
        arguments['allowLegends'] = False

    generations = request.args.get('gens')

    if generations:
        arguments['gens'] = list(filter(lambda a: a != 'undefined', generations.split()))
        print(arguments['gens'] )
        for i in range (0, len(arguments['gens'])):
            arguments['gens'][i] = int(arguments['gens'][i])

    pstyle = request.args.get('pstyle')
    if pstyle:
        arguments['pStyle'] = pstyle.lower()

    caprate = request.args.get('caprate')

    if caprate:
        arguments['minCapRate'] = float(caprate)


    myteam = request.args.get('myteam')
    mypokemon_lst = list(filter(lambda a: a != '', myteam.split("_")))
    myteam_dict = {}
    for pokemon in mypokemon_lst:
        new_lst = pokemon.split("6")
        new_lst = list(filter(lambda a: a != '', new_lst))
        new_lst = list(filter(lambda a: a != '%20%20%20%20%20%20%20%20%20%20%20%20', new_lst))

        moveset = []
        if len(new_lst) > 1:
            for i in range(1, len(new_lst)):
                moveset.append(new_lst[i])
        myteam_dict[new_lst[0]] = {'nature':None, 'moves':moveset}
    arguments['myTeam'] = myteam_dict

    theirteam = request.args.get('theirteam')
    theirteam_dict = {}
    if (theirteam):
        mypokemon_lst = list(filter(lambda a: a != '', theirteam.split("_")))
        for pokemon in mypokemon_lst:
            new_lst = pokemon.split("6")
            new_lst = list(filter(lambda a: a != '', new_lst))
            new_lst = list(filter(lambda a: a != '%20%20%20%20%20%20%20%20%20%20%20%20', new_lst))

            moveset = []
            if len(new_lst) > 1:
                for i in range(1, len(new_lst)):
                    moveset.append(move[i])
            theirteam_dict[new_lst[0]] = {'nature':None, 'moves':moveset}
    arguments['oppTeam'] = theirteam_dict

    league = request.args.get('league')
    if league:
        arguments['league'] = league
    else:
        arguments['league'] = 'NFE'




    results = generateResults(
        arguments['myTeam'],
        arguments['oppTeam'],
        arguments['allowLegends'],
        arguments['gens'],
        arguments['pStyle'],
        arguments['minCapRate'],
        league=arguments['league']
    )


    return render_template('results.html', imagedata=image_data, results=results)
