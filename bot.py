import Skype4Py
import json
import responses

class SugBot:
	def __init__(self, cfgfile):
		self.load_config(cfgfile)

	def load_config(self, cfgfile):
		print "Loading config"
		#open and parse json file
		cf = open(cfgfile, "r")
		config = json.load(cf)
		cf.close()

		# assign stuff according to config
		self.chatname = config['chatname']
		self.commands = config['commands']

	def start(self):
		print "Starting bot"
		self.skype = Skype4Py.Skype()
		self.skype.Attach()

		self.chat = self.skype.Chat(self.chatname)
		self._setupEventHandlers()

	def _setupEventHandlers(self):
		self.skype.RegisterEventHandler('MessageStatus', self.message_handler)

	def message_handler(self, Message, Status):
		if (Message.Chat == self.chat) and (Status != Skype4Py.cmsSending):
			if (Message.Body[0] == '!'):
				self._parse_command(Message.Body)

	def _parse_command(self, command):
		index = 0
		for i in range(0, len(self.commands)):
			if (command == self.commands[i]['chat_command']):
				index = i
				break
		response = ""
		if self.commands[i]['type'] == "text":
			response = self.commands[index]['response']
		else:
			func = getattr(responses, self.commands[index]['response'])
			response = func()

		self.chat.SendMessage(response);
		
