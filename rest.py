#!/usr/bin/env python
import web
import random  
import json
import requests

urls = (
    '/', 'index',
    '/API', 'api'
    
)

class index(object):
   
    def GET(self):
        return "TEST to see if webserver can run. PLEASE ADD /API to call the random API hits"
  
class api(object):
    def GET(self):
        json_dict={}
        json_dict["session"]= random.randint(0,7)        
        json_dict["kicks"] = int(json_dict["session"]) / 3
        json_dict["punches"] = int(json_dict["session"]) / 2
        json_dict["health"]= (json_dict["kicks"] * self.KICK() ) + (json_dict["punches"] * self.PUNCH() )
        web.header('Content-Type', 'application/json')
        return json.dumps(json_dict)

    def PUNCH(self):
        return 2   

    def KICK(self):
        return 3      

  

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

