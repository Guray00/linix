#!/usr/bin/env python3
import os
from PyInquirer import style_from_dict, Token, prompt, Separator
from clint.textui import puts, colored

def softwareChooser(categories, ID,  message):
	choices = []
	
	for j in categories:
		choices.append(Separator("\n== " + j.capitalize() + " =="))
		
		for s in categories[j]:
			choices.append({
				'name': s["display_name"].lower().capitalize()
			})
			

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


def swCategoryChooser(names, ID,  message):
	choices = []
	choices.append(Separator("\n== Categories =="))

	for i in names:
		choices.append({'name': i.capitalize()})

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


	
	
######################################################

#		MAIN FUNCTION HERE

######################################################
	
def installMenu(sw, style):
	
	if(len(sw) == 0):
		print(colored.red("[X] There isn't any supported software at the moment..."))
		print(colored.red(" -  Nothing will be installed"))
		return False

	avaiableSoftware = sw
	categories = []

	try:
		for key in avaiableSoftware:
			categories.append(key)

	except:
		pass

	answ = prompt(swCategoryChooser(categories,  "categories",  "Which categories are u interested in?"), style=style)

	# GET THE LIST OF PROGRAMS FROM SELECTED CATEGORIES
	choosenCategories = {}
	for i in answ["categories"]:
		key = i.lower()
		choosenCategories[key] = avaiableSoftware[key]


	# ASK FOR SPECIFIC SOFTWARE
	answ = prompt(softwareChooser(choosenCategories, "software", "Which software do u wanna install?"), style=style)

	software = []
	swHash = {}
	for key in avaiableSoftware:
		for s in avaiableSoftware[key]:
			value = s["display_name"].lower().capitalize()
			swHash[value] = s


	for s in answ["software"]:
		software.append(swHash[s])
	
	return software	
