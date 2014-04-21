import datetime

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getday(bot, args):
	today = datetime.datetime.today()
	index = today.weekday();
	return "Today it's " + week[index] + "."

def getweek(bot, args):
	today = datetime.datetime.today()
	year, week, day = today.isocalendar();
	return "Current week: " + str(week) + "."

def say(bot, args):
	msg = ""
	for str in args:
		msg += str + " "

	return msg