from datetime import datetime
import sys

class Logger:

	def __init__(self, outfile=None):
		if outfile == None:
			self.out = sys.stdout;
		else:
			self.out = open(outfile, "a") # We wan't to append to the file yo

		self.timefmtstring = "[%b %d %H:%M:%S]"

	def _get_timestring(self):
		return datetime.today().strftime(self.timefmtstring)

	def info(self, message):
		self.out.write(self._get_timestring() + "[INFO] " + message + "\n")

	def warn(self, message):
		self.out.write(self._get_timestring() + "[WARN] " + message + "\n")

	def error(self, message):
		self.out.write(self._get_timestring() + "[ERROR] " + message + "\n")