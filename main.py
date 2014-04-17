import sys
import bot

def main(argv):
	sugbot = bot.SugBot("config.json")
	sugbot.start()

if __name__ == "__main__":
	main(sys.argv)