import Skype4Py

# Create an instance of the skype class
skype = Skype4Py.Skype()

# Connect the skype object to the skype client
skype.Attach()

for x in skype.RecentChats:
	print x.Name

chatname = "#simonvmolzer/$fannynatta11;f553af0cfe503c07"

# Obtain some information from the client and print it out
print "Sending message in", chatname
chat = skype.Chat(chatname)
chat.SendMessage("Hello World!")