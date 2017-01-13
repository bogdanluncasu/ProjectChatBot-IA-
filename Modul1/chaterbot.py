from aiml import Kernel
from os import listdir
import os
import sys, processing
from flask import Flask, request
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
from collections import OrderedDict
import random,time

def set_personality(bot):
    bot.setBotPredicate("name", "Wasluianca")
    bot.setBotPredicate("gender", "robot")
    bot.setBotPredicate("master", "B2Group")
    bot.setBotPredicate("birthday", "21.12.2016")
    bot.setBotPredicate("birthplace", "Iasi")
    bot.setBotPredicate("boyfriend", "you")
    bot.setBotPredicate("favoritebook", "Stories from Vaslui")
    bot.setBotPredicate("favoritecolor", "blue")
    bot.setBotPredicate("favoriteband", "B.U.G Mafia")
    bot.setBotPredicate("favoritesong", "your voice")
    bot.setBotPredicate("forfun", "talktoyou")
    bot.setBotPredicate("friends", "you")
    bot.setBotPredicate("girlfriend", "you")
    bot.setBotPredicate("language", "english")
    bot.setBotPredicate("email", "wasluyanu@bot.ro")

files = listdir('standard')
bot = Kernel()
for file in files:
    bot.learn('standard/' + file)
set_personality(bot)	
substs = processing.get_substitutions()
respon = ' '
		
def ask_him(data,index,bot,substs,sessionId):
    question = data
    question = processing.apply_substitutions(question, substs)
    reply = bot.respond(question,sessionId)
    return "Bot> "+reply

class BotApplication(WebSocketApplication):

    def on_open(self):
        print "Connection opened"
        self.time=time.time()
        self.sessionId=random.randint(0,99999999)
        self.ws.send( "Bot> Hello , I am Wasluianca the bot. Good to see you. Type \"bye\" to exit")


    def on_message(self, message):
        if message!="":
            if bot is None or substs is None or message is None:
                pass
            else:
                reply = ask_him(message, 0,bot,substs,self.sessionId)
                self.time=time.time()
                self.ws.send(reply)
        elif time.time() - self.time > 30:
            reply = ask_him("INACTIVITATE", 0, bot, substs, self.sessionId)
            self.time = time.time()
            self.ws.send(reply)


    def on_close(self, reason):
        print reason
        self.ws.send("Bye")

WebSocketServer(
    ('', int(os.environ.get("PORT", 8000))),
    Resource(OrderedDict({'/': BotApplication}))
).serve_forever()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISTHESECRETKEY'


@app.route('/')
def welcome():
    return "Welcome",200



if __name__ == '__main__':
    try:
        app.run()
    except:
        pass