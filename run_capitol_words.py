#run_capitol_words.py
#script that calls the Capitol API to answer the question "which legislator has said the word 'coder' the most?
#==============================================================================================================

#Section 1: importing tools
#===============================================================
import requests
import pprint #Import the pretty print data reader 


#Section 2: Make the API call - ask it a question and save the answer in the variable r
#=================================================================

r = requests.get('http://capitolwords.org/api/1/phrases/legislator.json?phrase=coders&apikey=1ddfc51eee614c419f1ec873412e5485')

results = r.json() #saving the response of the API to the results varible, and translating json to python

#print results
Section

# 3: Will print out JUST the bioguide_id. 
#=================================================================
#print results['results'][0]['legislator'] 

#When you are working with lists of lists lists of dictionaries, on the same line, to print the item you want you have to break through each index.


#Section 4: Make another API call to get the name of the legislator that corresponds to that bioguide. 
#=================================================================
congress = results['results'][0]['legislator'] #setting the results of bioguide_id to the variable congress. 

url = 'http://congress.api.sunlightfoundation.com/legislators?apikey=1ddfc51eee614c419f1ec873412e5485&bioguide_id={0}'.format(congress)
# For a cleaner code, I am setting the API call to the variable 'url', then using the string format method to insert the bioguide_id
x = requests.get(url) #Setting x as the results of the API call
legislator_results = x.json() #Setting results to be translated from json text to python to the variable name. 
name = legislator_results['results'][0]['first_name']+" "+legislator_results['results'][0]['last_name']
prettyname = pprint.pprint(name) #Using the pretty print tool to show the results in a easy to read format
print prettyname


#Section 5: Modify your script so that it asks the user what word they want to search for and returns which legistator said it the most. 
#===============================================================

"""def word(): 

   phrase = raw_input("What phrase are you looking for? ")
   print phrase #This asks the user the question "What movie are you looking for?" and sets the variable of 'check'
    
   url = 'http://capitolwords.org/api/1/phrases/legislator.json?&apikey=1ddfc51eee614c419f1ec873412e5485&phrase={0}'.format(phrase)

   response = requests.get(url).json()
   prettyresponse = pprint.pprint(response)
   print response
get_word()"""