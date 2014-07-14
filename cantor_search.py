#cantor_search.py

#Section 1: Import tools
import requests
import pprint



#Section2: Call the API (make the Get request)

url = 'http://capitolwords.org/api/1/dates.json?phrase=Cantor&percentages=true&granularity=day&date=2014-06-11&apikey=1ddfc51eee614c419f1ec873412e5485'

cantor_mentions = requests.get(url).json()
cantor = cantor_mentions['results'][0]['count']



#Section 3: Print to the screen and format if necessary
print pprint.pprint(cantor_mentions)

print "The phrase 'Cantor' was said" + str(cantor)+ "times yesterday"
