#!/usr/bin/env python3

from PyInquirer import style_from_dict, Token, prompt, Separator
import json
import os
import sys
from clint.textui import puts, colored

DISTRO = sys.argv.index("--distro")+1
print(DISTRO)
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
	print(separator+"  "+"  / /    / //  |/ // / |   / "+"  "+separator)
	print(separator+"  "+" / /____/ // /|  // / /   |  "+"  "+separator)
	print(distance +"  "+"/_____/___/_/ |_/___//_/|_|  "+"  ")
	print(distance +" "+ colored.red("Your favourite bash installer\n"))

	distancePrint("If u don't know what u are doing, well, this is the right place!")
	distancePrint("Linix is a free-software simple as f*ck for fast configuration of")
	distancePrint("your OS, we both know that if u are here you destroyed something...")
	distancePrint("Therefore come on and config your machine (and pay attention next time)\n")
	
	
def questionMaker(names, ID,  message, category):
	choices = []
	
	i = 0
	for j in category:
		choices.append(Separator("\n== " + names[i] + " =="))
		
		for s in j:
			choices.append({
				'name': s["display_name"]
			})
		i+=1
			
	questions = [
	    {
		'type': 'checkbox',
		'message': message,
		'name': ID,
		'choices': choices,
		'validate': lambda answer: 'You must choose at least one program.' \
		    if len(answer) == 0 else True
	    }
	]	
	

	return questions
	

##########################################################################

#			PROGRAM STARTS HERE

#########################################################################

printLogo()

#for key in a_dict:
#	print(key, '->', a_dict[key])

# CATEGORY SETUP
basic = []
dev = []
gaming = []
cloud = []
graphics = []


categoriesString = ["basic", "dev", "gaming", "cloud", "graphics"]
categories = []


for i in categoriesString:
	tmp = {
  		"display_name": i
	}
	
	categories.append(tmp)


# IMPORTING JSONS
for file in os.listdir("./software/dev"):
	if file.endswith(".json"):
		tmp = json.loads(open(os.path.join("./software/dev", file), "r").read())
		dev.append(tmp)

for file in os.listdir("./software/basic"):
	if file.endswith(".json"):
		tmp = json.loads(open(os.path.join("./software/basic", file), "r").read())
		basic.append(tmp)		
   			
for file in os.listdir("./software/gaming"):
	if file.endswith(".json"):
		tmp = json.loads(open(os.path.join("./software/gaming", file), "r").read())
		gaming.append(tmp)

for file in os.listdir("./software/cloud"):
	if file.endswith(".json"):
		tmp = json.loads(open(os.path.join("./software/cloud", file), "r").read())
		cloud.append(tmp)

for file in os.listdir("./software/graphics"):
	if file.endswith(".json"):
		tmp = json.loads(open(os.path.join("./software/graphics", file), "r").read())
		graphics.append(tmp)
	
	
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


# ASK CATEGORY
try:
	answ = prompt(questionMaker(["Categories"], "categories", "Which categories are u interested in?", [categories]), style=style)


	software = []
	swHash = {}

	# GET THE LIST OF PROGRAMS FROM SELECTED CATEGORIES
	for i in answ["categories"]:

		tmp = []
		if (i == "basic"):
			for j in basic:
				tmp.append(j) 	
				swHash[j["display_name"]] = j	
		
		elif (i == "dev"):
			for j in dev:
				tmp.append(j)
				swHash[j["display_name"]] = j	
		
		elif (i == "gaming"):
			for j in gaming:
				tmp.append(j)
				swHash[j["display_name"]] = j
		
		elif (i == "cloud"):
			for j in cloud:
				tmp.append(j)
				swHash[j["display_name"]] = j
				
		elif (i == "graphics"):
			for j in graphics:
				tmp.append(j)
				swHash[j["display_name"]] = j
				
		software.append(tmp)
		
		
	# ASK FOR SPECIFIC SOFTWARE
	answ = prompt(questionMaker(["Basic", "Dev", "Gaming", "Cloud", "Graphics"], "software", "Which software do u wanna install?", software), style=style)

	software = []
	for i in answ["software"]:
		software.append(swHash[i])
		

	# RUNS THE INSTALLER
	#installerMain(software, "debian")


	platform = "deb"

	if (platform == "deb"):
		from debInstaller import debInstaller

		debInstaller(software)


	
except KeyError:
	print("Goodbye!")
	exit(0)
