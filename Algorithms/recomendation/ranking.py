from __future__ import division
import json
import math

class Feature():
    # Feature object, holds and id (string) and value (float)
    def __init__(self, _id, value):
        self.id = _id
        self.value = value

    def __repr__(self):
        # Overriding return of object Feature in print(feature)
        return self.id + ' ' + str(self.value)

    def __eq__(self, other):
        # A Feature is equal to the other if they share the same id
        if isinstance(other, Feature):
            return self.id == other.id
        return NotImplemented

class City():
    # City object, holds a name (string), features (array of Feature)
    def __init__(self, name, features):
        self.name = name
        self.features = features

    def __repr__(self):
        # Overriding return of object City in print(city)
        return self.name

class RankObject():
    # Rank object to be listed, city name (string) similarity with user query
    def __init__(self, cityName, similarity):
        self.city = cityName
        self.similarity = similarity

    def __repr__(self):
        # Overriding RankObject print statement
        return self.city + ' ' + str(self.similarity)

def normalizeValues(values):
    # Input: [(string, fload), (string, float), ...]
    # Output: [(string, fload), (string, float), ...]
    # The output will be in the strucutre, but with float values [0, 1]
    maxVal = max(map(lambda v: v[1], values))
    return map(lambda v: (v[0], v[1] / maxVal), values)

def normalizeFeatures(attractionsDict):
    # Returns on array of City objects with normalized feature values
    # [City1, City2, City3, ...]
    cities = {}
    for attId in attractionsDict:
        for normValue in normalizeValues(attractionsDict[attId]):
            cityName = normValue[0]
            attValue = normValue[1]
            if cities.get(cityName) == None:
                cities[cityName] = []
            cities[cityName].append(Feature(attId, attValue))
    return map(lambda val: City(val, cities[val]), cities)

def parseData(fp):
    # Returns a python dict indexed by feature and a list city/endorsement
    # {
    #    'feature1': [(CityName, endorsements), (CityName, endorsements), ...],
    #    'feature2': [(CityName, endorsements), (CityName, endorsements), ...],
    # }
    data = json.loads(open(fp, 'r').read().decode('utf-8'))
    attractionsDict = {}
    for key in data:
        attractions = data[key].get('attractions')
        endorsements = data[key].get('endorsement')
        for i in range(len(attractions)):
            attId = attractions[i].lower().encode('utf-8')
            attValue = float(endorsements[i])
            if attractionsDict.get(attId) == None:
                attractionsDict[attId] = []
            attractionsDict[attId].append((key, attValue))
    return attractionsDict

def loadCities(fp):
    # Returns a list of City objects with normalized Feature objects inside
    return normalizeFeatures(parseData(fp))

def seqSearch(array, key):
    # O(n) time complexity. Could be improved to O(log n) or O(1) depending
    # on data structure organization
    for i, val in enumerate(array):
        if val == key:
            return i
    return -1

def similarity(featureList1, featureList2):
    # Compute the mean absolute differece between featureList1 and featureList2
    # 0 means equal feature set
    sumOfDifferences = 0
    for feature in featureList1:
        featIndex = seqSearch(featureList2, feature)
        if featIndex != -1:
            sumOfDifferences += (feature.value - featureList2[featIndex].value)
        else:
            # if a user input is not found, compute anyway to penalize cities
            sumOfDifferences += feature.value

    return math.fabs(sumOfDifferences) / len(featureList1)

def featuresFromQuery(query):
    # receive a comma separated string, split by comma, and create a Feature
    # object with value 1 for each query word
    return map(lambda q: Feature(q.strip().lower(), 1), query.split(','))

def processQuery(userInput):
    # load and index the json file with data
    cities = loadCities('./data.json')

    # process the query into feature array
    userFeatures = featuresFromQuery(userInput)

    # rank cities by similarity with the user query feature array
    rank = []
    for city in cities:
        rank.append(
            RankObject(city.name, similarity(userFeatures, city.features)))

    return sorted(rank, key=lambda x: x.similarity)

def main():
    try:
        print 'Please enter your comma separated query, (example: architecture, city walks, walking)'
        query = str(raw_input('Query: '))
        # query = 'architecture, city walks, walking'
        rank = processQuery(query)
        print ""
        print 'Recommended city: ', rank[0].city + '!'
        print ""
        print "Ranking (most recommended first)"
        for i, r in enumerate(rank):
            print i + 1, ' ', r.city
    except KeyboardInterrupt:
        pass

main()
