#!/usr/bin/env python

import requests
import json
from sys import exit


def health(cur_health,cost):
   cur_health = int(cur_health) -  cost
   return cur_health

def CALL_API():
        url = 'http://10.100.7.19:8080/API'
        try:
        	response = requests.get(url)
        	json_data = json.loads(response.text)
        	player_did =[json_data['kicks'],json_data['punches'],json_data['health']]
        	return player_did
        except:
        	print "START rest.py before proceeding \n"
        	exit()

def action():
        Action = CALL_API()
        health_cost = int(Action[2])  
        description =  "Did " + str(Action[0]) + " kick " +  str(Action[1]) + " punch  cost " + str(Action[2])  +" life points \n"
        result = [description,health_cost]
        return result

def AI_WINS_OR_TIED(PLAYER_HEALTH,AI_HEALTH,user):
        print user +" HIT AI WITH THE FOLLOWING RESULTS:"
        while(PLAYER_HEALTH > AI_HEALTH):	
              FIGHT_RESULT2 = action()
              AI_HEALTH=health(INITIALIZE_HEALTH,FIGHT_RESULT2[1])
              if(PLAYER_HEALTH == AI_HEALTH):
              	print (FIGHT_RESULT2[0])
              	print "AI health has:", AI_HEALTH
              	print "Tied"	
              	break
              elif(PLAYER_HEALTH < AI_HEALTH):
              	print (FIGHT_RESULT2[0])
              	print "AI health has:", AI_HEALTH
              	print "AI WINS"	
              	break

REPEATEGAME = True
INITIALIZE_HEALTH = 50
user = raw_input ("Welcome to text fight!\n What is your name? ")
while (REPEATEGAME):

	REPEATEGAME = False
	FIGHT_RESULT = action()
	print "\n"	
	print "Welcome", user
	print user +"'s"+ " health is INITIALIZED TO: ", INITIALIZE_HEALTH
	print "AI health is INITIALIZED TO: ", INITIALIZE_HEALTH
	print "\n"	
	print "AI HITS " + user +" WITH THE FOLLOWING RESULTS:"
	print (FIGHT_RESULT[0])
	PLAYER_HEALTH=health(INITIALIZE_HEALTH,FIGHT_RESULT[1])
	print user + "'s"+" health is:", PLAYER_HEALTH
	
	FIGHT_RESULT2 = action()
	AI_HEALTH =health(INITIALIZE_HEALTH,FIGHT_RESULT2[1])
	if(PLAYER_HEALTH < AI_HEALTH):
		print user + " HITS AI WITH THE FOLLOWING RESULTS:"
		print (FIGHT_RESULT2[0])
		print "AI health has:", AI_HEALTH
		print "AI WINS"	
	elif(PLAYER_HEALTH == AI_HEALTH):
		print (FIGHT_RESULT2[0])
		print "AI health has:", AI_HEALTH
		print "Tied"	
		
	else:
		AI_WINS_OR_TIED(PLAYER_HEALTH,AI_HEALTH,user)

	game = raw_input ("Type yes to play again: ")
	if (game == "yes" or game == "y"): 
		REPEATEGAME = True
		INITIALIZE_HEALTH = 50
