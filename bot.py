import Skype4Py
import json

class SugBot:
	def __init__(self, cfgfile):
		self.loadconfig(cfgfile)

	def loadconfig(self, cfgfile):
		print "Loading config"
		#open and parse json file
		cf = open(cfgfile, "r")
		config = json.load(cf)
		cf.close()

		# assign stuff according to config
		self.chatname = config['chatname']

	def start(self):
		print "Starting bot"
		self.skype = Skype4Py.Skype()
		self.skype.Attach()

		self.chat = self.skype.Chat(self.chatname)
		self.chat.SendMessage("I'm in dude")