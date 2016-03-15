# Text-figher-rest

Simple text base game written in Python

Rules:

1. There are 2 players, one of them is an AI
2. Total hit points of each player is 50
3. A punch will cost an opponent 2 hit points
4. A kick will cost an opponent 3 hit points

Framework

Used Web.py to simulate a simple RESTful web API

Setup 

1.  Run rest.py
2.  Run play.py


API

	Running the rest.py will create a simple webserver.  In order to get the response you must call the address of the webserver created by rest.py with /API.  The response will be a simple JSON format of punch , kick , and total damage.

 Sample:
    localhost:8080/API -  this will have a simple JSON response

To play the game:

  1. Run play.py.  
  2. The program will ask for your name.
  3. The text will now display  the player's turn then the AI's turn together with the number of punches and kicks.
  4. Whoever has more hit points wins.
  5. Enjoy!

  note:  The AI player doesn't loose