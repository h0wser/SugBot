SugBot --- A fancy skype bot
========

Features
----
* Custom commands (ex !day -> "It's Monday.")
* Timed messages (MOTD, Info messages) (not done)
* Op powers (not done)
* JSON config file

Requirements
-----
* Skype for Linux
* [Skype4Py](https://github.com/awahlig/skype4py)
* Python 2

Usage
---
__Install/Download:__

	clone git repo blabla

__Run:__

	prompt> python main.py

This project is made using python 2.7 and not 3. Make sure that you use the correct python version when running.
On arch for example, the program is run with:
	
	prompt> python2 main.py

Config: 
-----
The bot's behaviour is controlled via 2 files: config.json and responses.py.

**_config.json_** tells the bot of the name of the chat and what types of messages/commands there are.

The __commands__ array details what the bot does with a "!xxcommand" message sent in the chat it's listening to. 
Every object in commands has 3 properties: chat_command, response, type

* __chat_command__ is a string that represents this command in chat 
* __response__ is either a message string containing a response __or__ the name of a function that is defined in _responses.py_
* __type__ can be _text_ or _call_ and defines how __response__ is interperted

The __timed_messages__ array contains messages that are to be sent at a specific time. 
Every object in timed_messages has 2 properties: message and time

* __message__ is the message to be sent 
* __time__ is the time at which to send the message(duuh). The format is HH:MM:SS

**_responses.py_** defines functions referenced by the json in _config.json_.

The functions must return a string which will be the message sent to the chat.

__Example:__

	def foo()
		bar = "message"
	return bar
	
You can use any type of python code, in _responses.py_, to implement the message returned. Because of this, the possibilty of customization is endless.