from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "SquadUp"
net_ids = [
           "Sherry Xie: zx53" ,
           "Jesse Phillip: jop23",
           "Kelly Fam: kjf63",
           "Trevor Jamison: tj222",
           "Boonakij Palipatana: bap93"
          ]

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netids=net_ids, output_message=output_message, data=data)



