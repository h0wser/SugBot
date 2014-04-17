import sys
import bot

def main(argv):
	sugbot = bot.SugBot("config.json")
	sugbot.start()
	while True:
		pass

if __name__ == "__main__":
	main(sys.argv)