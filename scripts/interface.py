#!/usr/bin/env python3

from PyInquirer import style_from_dict, Token, prompt, Separator
import os
import sys
from clint.textui import puts, colored
import json

from installMenu import installMenu

DISTRO = sys.argv[sys.argv.index("--distro")+1]				#gets the running distro
rows, columns = os.popen('stty size', 'r').read().split()
	
def distancePrint(string):
	distanceSize = int((int(columns) - len(string))/2)
	d = ' '*distanceSize
	print(d+string) 
	
def printLogo():
	distanceSize = (int(columns) - 30-4)/2

	distance      = ' '*int(distanceSize)
	separator     = colored.red('='*int(distanceSize))

	print(distance +"  "+"    __    _____   _______  __"+"  ")
	print(distance +"  "+"   / /   /  _/ | / /  _/ |/ /"+"  ")
	print(separator+"  "+"  / /    / //  |/ // / |   / "+"  "+separator+colored.red("="))
	print(separator+"  "+" / /____/ // /|  // / /   |  "+"  "+separator+colored.red("="))
	print(distance +"  "+"/_____/___/_/ |_/___//_/|_|  "+"  ")
	print(distance +" "+ colored.red("Your favourite bash installer\n"))

	distancePrint("If u don't know what u are doing, well, this is the right place!")
	distancePrint("Linix is a free-software simple as f*ck for fast configuration of")
	distancePrint("your OS, we both know that if u are here you destroyed something...")
	distancePrint("Therefore come on and config your machine (and pay attention next time)\n")
	
def jsonParser():
	avaiableSoftware = {}
	badJson = []
	
	for file in os.listdir("./software/"):
		if (file.endswith(".json") and file != "template.json"):
			
			try:
				original = json.loads(open(os.path.join("./software/", file), "r").read())
			except:
				badJson.append(file)
				continue
			
			tmp = {}
			
			try:
				tmp["display_name"] = original["display_name"]

				try:	category = original["category"].lower()
				except: category = "other"

				for key in original[DISTRO]:
					tmp[key] = original[DISTRO][key]
					
				try: 
					avaiableSoftware[category].append(tmp)

				except:
					avaiableSoftware[category] = []						
					avaiableSoftware[category].append(tmp)
					
			except:
				badJson.append(file)
				pass


	if (len(badJson) > 0):
		for i in badJson:
			print(colored.yellow("[W] WARNING: Bad json implemented: " +i))

		print(colored.green("Continuing, NON fatal error."))
		input(colored.green("Press [ENTER] to continue: "))
		os.system("clear")
		
	return avaiableSoftware




##########################################################################

#					PROGRAM STARTS HERE

#########################################################################



avaiableSoftware = jsonParser()
printLogo()


# SETTING UP GUI COLORS			
style = style_from_dict({
    Token.Separator: '#FF0000',   #cc5454
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})



try:

	#TODO: choose if u wanna install, config, run scripts etc

	wannaInstall = True

	if (wannaInstall):
		software = installMenu(avaiableSoftware, style)

	if (DISTRO == "DEBIAN"):

		if (wannaInstall):
			from debInstaller import debInstaller
			debInstaller(software)

	else:
		print(colored.red("Your distro isn't supported yet, I'm sorry."))
	
except:
	print("Goodbye!")
	exit(0)
