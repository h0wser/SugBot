import datetime

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getday():
	today = datetime.datetime.today()
	index = today.weekday();
	return "Today it's " + week[index] + "."

def getweek():
	today = datetime.datetime.today()
	year, week, day = today.isocalendar();
	return "Current week: " + str(week) + "."