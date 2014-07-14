#Section 1: importing tools

import requests 


#Section 2: script that calls the Bechdel API to find out a movice of your choice and print the results.

response = requests.get('http://capitolwords.org/api/1/phrases/legislator.json?phrase=coders&&apikey=1ddfc51eee614c419f1ec873412e5485')

results = response.json() #will print the results of the requests

#for r in results:
	#print r['year'], r['title']


print results