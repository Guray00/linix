#!/usr/bin/env python3
import sys
import os
from clint.textui import puts, colored

def getTimes():
	file  = open("/tmp/linix", "r")
	times = int(file.readline().replace("\n", ""))
	return times

def boldText(string):
	return colored.blue(string)


destination  = sys.argv[2]
searchPhrase = sys.argv[1]

os.system('grep "' + searchPhrase + '" '+ destination +' | wc -l > /tmp/linix')
if (getTimes() == 0):
	print(colored.green("string[Ok] Adding the source to the file"))
	command = "sudo sh -c 'echo \"deb " + searchPhrase + '" >> ' + destination + "'"
	print("Running command: " + command)
	os.system(command)
	print("Done, continuing.")
else:
	print(colored.green("[NO] Source already added, continuing."))
