import json 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression

vectorizer = TfidfVectorizer(max_features=50)

def generateClassifiers(traindata, summaries):
    classifiers = {}
    for league, obj in traindata.items():
        X_train = [summaries[pkmn] for pkmn, score in obj.items()]
        y_train = [score for pkmn, score in obj.items()]
        vectors = vectorizer.fit_transform(X_train)
        clf = LinearRegression().fit(vectors, y_train)
        classifiers[league] = clf
    return classifiers

def vectorizeTestData(summaries):
    docs = [value for key, value in summaries.items()]
    vectors = vectorizer.fit_transform(docs)
    return vectors

def predict(clfs, league, testdata):
    clf = clfs[league]
    return clf.predict(testdata)

summaries = json.load(open('dataset/PokemonToSummaries.json'))
traindata = json.load(open('dataset/trained_data.json'))

classifiers = generateClassifiers(traindata, summaries)
testdata = vectorizeTestData(summaries)

weights = {} 
for key, value in traindata.items():
    league_weights = predict(classifiers, key, testdata).tolist()
    league_mappings = {}
    for i in range(len(league_weights)):
        pkmn = list(summaries.keys())[i]
        wt = league_weights[i]
        if pkmn in traindata[key].keys():
            league_mappings[pkmn] = traindata[key][pkmn]
        else:
            league_mappings[pkmn] = wt
    weights[key] = league_mappings

with open('dataset/classWeights2.json','w') as outfile: 
    json.dump(weights, outfile)