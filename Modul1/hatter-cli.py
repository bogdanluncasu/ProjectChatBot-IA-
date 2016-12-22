# Hatter command line version, This doesn't require Flask
from aiml import Kernel
from os import listdir
import sys, processing

def set_personality(bot):
	bot.setBotPredicate("name", "PCH")
	bot.setBotPredicate("gender", "robot")
	bot.setBotPredicate("master", "B2Group")
	bot.setBotPredicate("birthday", "21.12.2016")
	bot.setBotPredicate("birthplace", "Iasi")
	bot.setBotPredicate("boyfriend", "you")
	bot.setBotPredicate("favoritebook", "Dont't read me")
	bot.setBotPredicate("favoritecolor", "transparent")
	bot.setBotPredicate("favoriteband", "B.U.G Mafia")
	bot.setBotPredicate("favoritesong", "your voice")
	bot.setBotPredicate("forfun", "talktoyou")
	bot.setBotPredicate("friends", "you")
	bot.setBotPredicate("girlfriend", "you")
	bot.setBotPredicate("language", "english")
	bot.setBotPredicate("email", "pch@bot.romania")


files = listdir('standard')

bot = Kernel()
for file in files:
	bot.learn('standard/'+file)

set_personality(bot)
substs = processing.get_substitutions()
respon = ' '
print "Bot> Hello , I am PCH the bot. Good to see you. Type \"bye\" to exit"

while 1 :
	question = raw_input("You> ")
	question = processing.apply_substitutions(question, substs)
	reply = bot.respond(question)
	print "Bot> ",reply
	if question == "bye":
		sys.exit(0)
		
