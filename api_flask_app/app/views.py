# -*- coding: utf-8 -*-
#Section 1: import tools
from app import app
from flask import render_template
import requests

@app.route('/')
def index():
#Section2: Call the API (make the Get request)
	#url = 'http://capitolwords.org/api/1/dates.json?phrase=Cantor&percentages=true&granularity=day&date=2014-06-11&apikey=1ddfc51eee614c419f1ec873412e5485'
	#cantor_mentions = requests.get(url).json() #This gives you a dictionary results
	#cantor = cantor_mentions['results'][0]['count'] # This is slicing through the index

	url = 'http://capitolwords.org/api/1/phrases/legislator.json?phrase=yolo&sort=count&apikey=1ddfc51eee614c419f1ec873412e5485'
	yolo_mentions = requests.get(url).json()
	yolo = yolo_mentions['results'][0]['count']

	return (yolo)

	#url_3 = 'http://congress.api.sunlightfoundation.com/legislators?bioguide_id=T000460&apikey=1ddfc51eee614c419f1ec873412e5485'
	#yolo_said = requests.get(url_3).json()
	#said = yolo_said['results'][0]['first_name']+" "+['results'][0]['last_name']

	#return (said)
#Section 3: Print to the screen and format into a string
	#return("The phrase 'Cantor' was said" +" "+ str(cantor)+ " "+ "times yesterday!")
	#return ("the phrase 'yolo' was said"+" "+str(yolo)+" "+"by"+" "+said)