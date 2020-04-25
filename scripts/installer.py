#!/usr/bin/env python3
from clint.textui import puts, colored
from os import path
import os
rows, columns = os.popen('stty size', 'r').read().split()


class Installer:
    alreadyInstalled = []
    pkgs             = []
    errors           = []
    pending = {}
    
    def errorMessage(self, i):
	    print(colored.red("Something went wrong, i'm sorry..."))
	    self.errors.append(i)


    def MUST4WORK(self):
        return

    def printInstalling(self, i):
        string = "  Installing "+i["name"]+"...  "
        distanceSize = int((int(columns) - len(string))/2)
        d = '='*distanceSize
        print("\n"+colored.yellow(d+string+d))
    		
    def printResults(self):							# print the result of the program, like
        if (len(self.pkgs) > 0 ):	                # installed softwares, errors ecc 
            self.printSeparator()
            print("\n"+colored.green(str(len(self.pkgs)))+" programs had been installed: ")
            for i in self.pkgs:
                print("   -"+ i["display_name"])

        if (len(self.alreadyInstalled)>0):	
                print("\n"+colored.blue(str(len(self.alreadyInstalled)))+" programs were already installed: ")
                for i in self.alreadyInstalled:
                    print("   -"+i["display_name"])
        
        print("\n")

    def installedCheck(self, i):							# checks if a program is already installed
        return

    def checkInstallMethod(self, i):						# checking the installation method (debian)
        return False

    def installAll(self):
        return False

    def printSeparator(self):
        separatorFull = colored.red('='*int(columns))
        print("\n"+separatorFull)

################################################
#                    INIT
################################################

    def __init__(self, software):
        self.software = software

        self.printSeparator()
        self.MUST4WORK()

        for i in software:
            installed = self.installedCheck(i)

            if (not installed):					# i install only if it is not already installed...
                self.pkgs.append(i)
                method = self.checkInstallMethod(i)

                try:
                    self.pending[method].append(i)
                
                except:
                    self.pending[method] = []
                    self.pending[method].append(i)

            else:
                self.alreadyInstalled.append(i)

            
        if (len(self.pending) > 0):
                self.installAll()
        
        self.printResults()