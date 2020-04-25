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
    
    # PRINT ERROR MESSAGE
    def errorMessage(self, i):
	    print(colored.red("Something went wrong, i'm sorry..."))
	    self.errors.append(i)

 
    # PRINT FANCY INSTALLING
    def printInstalling(self, i):
        string = "  Installing "+i["name"]+"...  "
        distanceSize = int((int(columns) - len(string))/2)
        d = '='*distanceSize
        print("\n"+colored.yellow(d+string+d))
    
    #PRINT AT THE END OF THE PROGRAMS SOME STATS
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

    # PRINT FANCY SEPARATOR
    def printSeparator(self):
        separatorFull = colored.red('='*int(columns))
        print("\n"+separatorFull)

    # INSTALL MUST HAVE DEPENDECIES (-> OVERRIDE <-)
    def MUST4WORK(self):
        return False

    #CHECKS IS SW IS INSTALLED (->OVERRIDE<-)
    def installedCheck(self, i):							# checks if a program is already installed
        return False

    #CHECKS THE RIGHT INSTALLATION METHOD (-> OVERRIDE <-) 
    def checkInstallMethod(self, i):						# checking the installation method (debian)
        return False

    #INSTALL ALL PROGRAMS (-> OVERRIDE <-)
    def installAll(self):
        return False

  
################################################
#                    INIT (NO override)
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