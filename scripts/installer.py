#!/usr/bin/env python3

import os
import sys
import apt
from os import path
from pathlib import Path
from clint.textui import puts, colored

cache = apt.Cache()
cache.open()


# ARRAYS
alreadyInstalled = []
aptPackages = []
snapPackages = []
dpkgPackages = []
errors = []



def errorMessage(i):
	print(colored.red("Something went wrong, i'm sorry..."))
	errors.append(i)

def MUST4WORK():							# Needed dependecies
	if(not cache["wget"].is_installed):
		os.system("sudo apt install dpkg-core wget -y")
	
	if(not cache["curl"].is_installed):
		os.system("ssudo apt install curl -y")
	
	if(not cache["git"].is_installed):
		os.system("sudo apt install git -y")
		
		
def printResults():							# print the result of the program, like
	pkgs = aptPackages						# installed softwares, errors ecc
	
	for i in snapPackages:
		pkgs.append(i)
		
	for i in dpkgPackages:
		pkgs.append(i["name"])
	
	if (len(pkgs) > 0 ):	
		print("\n\n"+colored.green(str(len(pkgs)))+" programs had been installed: ")
		for i in pkgs:
			print("   -"+i)

	if (len(alreadyInstalled)>0):	
			print("\n\n"+colored.blue(str(len(alreadyInstalled)))+" programs had been alredy installed: ")
			for i in alreadyInstalled:
				print("   -"+i["name"])
	
	print("\n")
			
			
def installedCheck(i):							# checks if a program is already installed
	installed = False
		
	if(i["method"] != "snap"):
		try:
			installed = cache[i["name"]].is_installed
		except:
			pass
	
	else:
		if(path.exists(str(Path.home())+"/snap/"+i["name"])):	# if the file is a snap, to check if it is installed
			installed = True				# i need to see the /home/snap folder and check if it is there

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
	
	
def checkInstallMethod(i):						# checking the installation method (debian)
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
	
		
		if (not installed):					# i install only if it is not already installed...				
			method = checkInstallMethod(i) 
			if(method == "apt"):
				aptPackages.append(i["name"])		# adding the name of the packages to the list of apt
			
			elif(method == "snap"):				# adding the name of the packages to the list of apt
				snapPackages.append(i["name"])
			
			elif(method == "dpkg"):				# installing from file list
				dpkgPackages.append(i)
			
				
		else:
			alreadyInstalled.append(i)
		
	if(len(aptPackages) > 0):
		os.system("sudo apt update")				# apt update is slow, i run it only if i need (so for apt)
	
	for i in aptPackages:
		os.system("sudo apt install " + i+" -y")		
		
	for i in snapPackages:
		os.system("sudo snap install "+ i + " --classic")	
	
	for i in dpkgPackages:
		os.system(i["wget"])
		os.system("sudo dpkg -i "+i["dpkg"])
		
	if (len(dpkgPackages) > 0):
		os.system("sudo apt-get -f install -y")
	
	printResults()
	
	
		
	return
