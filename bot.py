import Skype4Py
import json
import responses
import datetime
import time
from logger import Logger

class SugBot:
	def __init__(self, cfgfile):
		self.logger = Logger()
		self.load_config(cfgfile)

	def load_config(self, cfgfile):
		self.logger.info("Loading config")
		#open and parse json file
		cf = open(cfgfile, "r")
		config = json.load(cf)
		cf.close()

		# assign stuff according to config
		self.chatname = config['chatname']
		self.commands = config['commands']

		self.timed_messages = config['timed_messages']

		for msg in self.timed_messages:
				hour, minutes, seconds = msg['time'].split(":", 2)
				hour = int(hour); minutes = int(minutes); seconds = int(seconds)
				msg['time'] = datetime.time(hour, minutes, seconds)
				msg['sent'] = msg['time'] < datetime.datetime.now().time()

	def start(self):
		self.logger.info("Starting bot")
		self.skype = Skype4Py.Skype()
		self.skype.Attach()

		self.chat = self.skype.Chat(self.chatname)
		self._setupEventHandlers()

		self._handle_timed_messages();

	def _setupEventHandlers(self):
		self.skype.RegisterEventHandler('MessageStatus', self.message_handler)

	def message_handler(self, Message, Status):
		if (Message.Chat == self.chat) and (Status == Skype4Py.cmsReceived):
			if (Message.Body[0] == '!'):
				self._parse_command(Message.Body)

	def _parse_command(self, command):
		index = 0
		send = False
		args = command.split(" ")
		command = args.pop(0)

		for i in range(0, len(self.commands)):
			if (command == self.commands[i]['chat_command']):
				index = i
				send = True
				break

		response = ""
		if self.commands[i]['type'] == "text":
			response = self.commands[index]['response']
		else:
			func = getattr(responses, self.commands[index]['response'])
			response = func(self, args)

		if send:
			self.chat.SendMessage(response)

	def _handle_timed_messages(self):
		while True:
			for msg in self.timed_messages:
				if msg['time'] < datetime.datetime.now().time() and msg['sent'] == False:
					self.chat.SendMessage(msg['message'])
					msg['sent'] = True

			if (datetime.datetime.now().time() < datetime.time(0, 1, 30)):
			 	for msg in self.timed_messages:
			 		msg['sent'] = False

			time.sleep(5)