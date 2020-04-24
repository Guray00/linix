#!/usr/bin/env python3


from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
#from pprint import pprint
#from pyfiglet import Figlet
import json
import os
from installer import installerMain
from clint.textui import puts, colored



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

#f = Figlet(font='slant')
#print (f.renderText('LINIX'))


rows, columns = os.popen('stty size', 'r').read().split()

distanceSize = (int(columns) - 30-4)/2

distance      = ' '*int(distanceSize)
separator     = colored.red('='*int(distanceSize))



print(distance +"  "+"    __    _____   _______  __"+"  ")
print(distance +"  "+"   / /   /  _/ | / /  _/ |/ /"+"  ")
print(separator+"  "+"  / /    / //  |/ // / |   / "+"  "+separator)
print(separator+"  "+" / /____/ // /|  // / /   |  "+"  "+separator)
print(distance +"  "+"/_____/___/_/ |_/___//_/|_|  "+"  ")
print(distance + colored.red("Your favourite bash installer\n\n"))

basic = []
dev = []
gaming = []
cloud = []

categoriesString = ["basic", "dev", "gaming", "cloud"]
categories = []

for i in categoriesString:
	tmp = {
  		"display_name": i
	}
	
	categories.append(tmp)


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
		
style = style_from_dict({
    Token.Separator: '#FF0000',   #cc5454
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


answ = prompt(questionMaker(["Categories"], "categories", "Which categories are u interested in?", [categories]), style=style)



software = []

swHash = {}

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
	software.append(tmp)
	
	
answ = prompt(questionMaker(["Basic", "Dev", "gaming", "cloud"], "software", "Which software do u wanna install?", software), style=style)

software = []
for i in answ["software"]:
	software.append(swHash[i])
	


installerMain(software)


	

