#!/usr/bin/env python3
import sys
import os

def getTimes():
	file  = open("/tmp/linix", "r")
	times = int(file.readline().replace("\n", ""))
	return times

def boldText(string):
	return "\e[1m"+string+"\e[22m"

argv = sys.argv[1]
destination  = argv.split(" >> ")[1]
searchPhrase = argv.split(" >> ")[0].split('"')[1]


os.system('grep "' + searchPhrase + '" '+ destination +' | wc -l > /tmp/linix')
if (getTimes() == 0):
	print("[Ok] Adding the source to the file")
	command = "sudo sh -c 'echo \"" + searchPhrase + '" >> ' + destination + "'"
	print("Running command: " + command)
	os.system(command)
	print("Done, continuing.")
else:
	print("[NO] Source already added, continuing.")
