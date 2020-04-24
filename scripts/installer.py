#!/usr/bin/env python3

import os
import sys
import apt
from os import path
from pathlib import Path
from clint.textui import puts, colored

cache = apt.Cache()
cache.open()


alreadyInstalled = []
aptPackages = []
snapPackages = []
dpkgPackages = []
errors = []



def errorMessage(i):
	print(colored.red("Something went wrong, i'm sorry..."))
	errors.append(i)

def MUST4WORK():
	if(not cache["wget"].is_installed):
		os.system("sudo apt install dpkg-core wget -y")
	
	if(not cache["curl"].is_installed):
		os.system("ssudo apt install curl -y")
	
	if(not cache["git"].is_installed):
		os.system("sudo apt install git -y")
		
		
def printResults():
	pkgs = aptPackages
	
	for i in snapPackages:
		pkgs.append(i)
		
	for i in dpkgPackages:
		pkgs.append(i["name"])
	
	if (len(pkgs) > 0 ):	
		print("\n\n"+colored.green(str(len(pkgs)))+" program had been installed: ")
		for i in pkgs:
			print("   -"+i)

	if (len(alreadyInstalled)>0):	
			print("\n\n"+colored.blue(str(len(alreadyInstalled)))+" program had been alredy installed: ")
			for i in alreadyInstalled:
				print("   -"+i["name"])
	
	print("\n")
			
def installedCheck(i):
	installed = False
		
	if(i["method"] != "snap"):
		try:
			installed = cache[i["name"]].is_installed
		except:
			pass
	else:
		if(path.exists(str(Path.home())+"/snap/"+i["name"])):
			installed = True

	return installed

def ppaAdder(i):
	try:
		os.system("sudo add-apt-repository ppa:"+i["ppa"]+" -y")
	except:
		errorMessage(i)
		
def sourceAdder(i):
	try:
		os.system(i["pgp"])
		os.system("python3 ./scripts/add_source.py "+ i["deb"] + " "+ i["dest"])
		
	except:
		errorMessage(i)
	return
	
def checkInstallMethod(i):
	try:
		method = i["method"] 
		
		if (method == "ppa"):
			ppaAdder(i)
			return "apt"
		
		elif(method == "source"):
			sourceAdder(i)
			return "apt"
			
		elif(method == "apt"):
			return "apt"
		
		elif(method == "snap"):
			return "snap"

		elif(method == "dpkg"):
			return "dpkg"
		
		else:
			print("NON SUPPORTED.... ABORTED")
			errors.append(i)
			return False
	except:
		errorMessage(i)

	return false
	
def installerMain(software):
	rows, columns = os.popen('stty size', 'r').read().split()
	separatorFull = colored.red('='*int(columns))
	print(separatorFull)
	MUST4WORK()
	
	for i in software:
		installed = installedCheck(i)
	
		
		if (not installed):
			method = checkInstallMethod(i) 
			if(method == "apt"):
				aptPackages.append(i["name"])
			
			elif(method == "snap"):
				snapPackages.append(i["name"])
			
			elif(method == "dpkg"):
				dpkgPackages.append(i)
			
				
		else:
			alreadyInstalled.append(i)
		
	if(len(aptPackages) > 0):
		os.system("sudo apt update")
	
	for i in aptPackages:
		os.system("sudo apt install " + i)
		
	for i in snapPackages:
		os.system("sudo snap install "+ i + " --classic")	
	
	for i in dpkgPackages:
		os.system(i["wget"])
		os.system("sudo dpkg -i "+i["dpkg"])
		
	if (len(dpkgPackages) > 0):
		os.system("sudo apt-get -f install -y")
	
	printResults()
	
	
		
	return
