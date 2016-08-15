Author:
----------------------
Nikolas Moya
nikolasmoya@gmail.com
http://nikolasmoya.com

Items:
----------------------
    - readme.txt exaplanation file
    - ranking.py code file
    - data.json data file



Requirements:
----------------------
Python 2.7 (already installed in unix systems)



Usage:
----------------------
Leave data.json and ranking.py at the same folder and execute:

python ranking.py

You will be prompted to enter a comma separated query for the search engine, for example: architecture, city walks, walking

The output will be a sorted rank where the first position is the most recommended city and the last position is the least recommended city.



Explanation:
----------------------
I implemented a simple user-item recommendation system. The sample data provided in the problem description was converted to a json file (data.json).
This file is parsed into memory and the features are normalized within [0, 1]. In order to compute this normalization, I selected all the endorsement values
from features that share the same id (attraction name) and divided by the maximum value.

After the parsing, we should have an array of cities, each city with a name and a feature array.
Lisboa: [city walks 0.790072189092, culture 0.410829380525, food 0.702597016194, monuments 0.440154964997, ...]
Amsterdam: [city walks 1.0, walking 1.0, shopping 0.471152087221, culture 0.512835463385, museums 0.761271860847, ...]
Paris: [shopping 1.0, culture 1.0, food 1.0, monuments 1.0, museums 1.0, architecture 1.0, art 1.0, history 1.0, sightseeing 1.0]

The user query is converted into a feature array. So architecture, city walks, walking becomes: [Feature('architecture', 1), Feature('city walks', 1), Feature('walking', 1)]
The user feature array is then compared to the feature array of every city from the parsed data. A similarity measure is used to compute the euclidean distance between feature sets.
The smaller the number, the closer the feature sets are, thus more recommended that city is for the given query.

The results are sorted in ascending order of similarity and displayed.

Example output:
Query: architecture, city walks, walking

Recommended city:  Amsterdam!

Ranking (most recommended first)
1  -  Amsterdam 0.129439687547
2  -  Lisboa 0.579172271655
3  -  Paris 0.666666666667


Even though Paris is the feature leader of architecture, since it lacks 'city walks' and 'walking' features,
it was ranked worst than Amsterdam and Lisboa that have more points in walking attractions (See feature array above).



Considerations:
----------------------
- Simple implementation with room for improvement: Ex. Replace lists with a more appropriate data structure to improve feature set search time (Bloom filters, for example).
- Summing the endorsement are definitely not enough to properly rank the cities. Normalization is necessary so all the data is proportionally in the same range.
- Joke endorsements could be filtered by further classifying the endorsement values. A simple way would be consider only endorsements with value > max(endorsements) / 2.
