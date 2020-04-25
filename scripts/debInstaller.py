#!/usr/bin/env python3
import apt
from os import path
import os
from pathlib import Path
from installer import Installer
from clint.textui import puts, colored

cache = apt.Cache()
cache.open()

class debInstaller( Installer ):
    
    def MUST4WORK(self):
        if(not cache["wget"].is_installed):
            os.system("sudo apt install dpkg-core wget -y")
            
        if(not cache["curl"].is_installed):
            os.system("ssudo apt install curl -y")
            
        if(not cache["git"].is_installed):
            os.system("sudo apt install git -y")

    def ppaAdder(self, i):
        try:
            command = i["key"]
            os.system(command)
	
        except:
            pass

        try:
            os.system("sudo add-apt-repository "+i["ppa"]+" -y")
        except:
            self.errorMessage(i)


    def sourceAdder(self, i):
        try:
            os.system(i["pgp"])
            os.system("python3 ./scripts/add_source.py "+ i["deb"] + " "+ i["dest"]) 
		
        except:
            self.errorMessage(i)
        
        return

    def checkInstallMethod(self, i):
        try:
            method = i["method"] 
                
            if (method == "ppa"):
                self.ppaAdder(i)
                return "apt"
                
            elif(method == "source"):
                self.sourceAdder(i)
                return "apt"

            elif(method == "apt"):
                return "apt"
            
            elif(method == "snap"):
                return "snap"

            elif(method == "dpkg"):
                return "dpkg"
            
            else:
                print("NON SUPPORTED.... ABORTED")
                self.errors.append(i)
                return False

        except:
            self.errorMessage(i)

        return False


    def installedCheck(self, i):							# checks if a program is already installed
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

    def installAll(self):
        try:
            if(len(self.pending["apt"]) > 0):
                string = "  Updating apt  "
                rows, columns = os.popen('stty size', 'r').read().split()

                distanceSize = int((int(columns) - len(string))/2)
                d = '='*distanceSize

                print("\n"+colored.green(d+string+d))
                os.system("sudo apt update")

        except:
            pass

        for key in self.pending:
            #print(key, '->', a_dict[key])
                    
            for i in self.pending[key]:
                self.printInstalling(i)

                if(key == "apt"):
                    os.system("sudo apt install " + i["name"]+" -y")
                                            
                elif(key == "snap"):				    # adding the name of the packages to the list of apt
                    os.system("sudo snap install "+ i["name"] + " --classic")
                        
                elif(key == "dpkg"):				    # installing from file list
                    os.system(i["wget"])
                    os.system("sudo dpkg -i "+i["dpkg"])

        try:
            if(len(self.pending["dpkg"]) > 0):
                os.system("sudo apt-get -f install -y")
        
        except:
            pass