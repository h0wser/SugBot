import sys
import signal
import bot

sugbot = bot.SugBot("config.json")

def main(argv):
	
	sugbot.start()

def sigint_handler(signum, frame):
	print "--== Exiting ==--"
	sugbot.exit()
	sys.exit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, sigint_handler)
	main(sys.argv)