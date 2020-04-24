#!/bin/bash

#INSTALLAZIONI FONDAMENTALI
sudo apt install git -y
sudo apt install curl -y
sudo apt install python3 -y
sudo apt install python3-pip -y

#ADDING PGP KEYS
wget -O - http://deb.opera.com/archive.key | sudo apt-key add - #opera-stable
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | sudo apt-key add - #vscodium
curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
#sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 0xd66b746e #skype

# AGGIUNTA DELLE SOURCE PER I PROGRAMMI
clear
echo "ADDING SOURCES --------------------"
python3 add_source.py 'echo "deb http://deb.opera.com/opera-stable/ stable non-free" >> /etc/apt/sources.list.d/opera.list' 
python3 add_source.py 'echo "deb https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/repos/debs/ vscodium main" >> /etc/apt/sources.list.d/vscodium.list' 
python3 add_source.py 'echo "deb https://apt.syncthing.net/ syncthing stable" >> /etc/apt/sources.list.d/syncthing.list'
#python3 add_source.py 'echo "deb http://download.skype.com/linux/repos/debian/ stable non-free" >> /etc/apt/sources.list'

#AGGIUNTA PPA
clear
echo "SOURCE ADDED ----------------------"
echo "ADDING PPA ------------------------"
sudo add-apt-repository ppa:atareao/telegram -y
sudo apt update 

#INSTALLAZIONI DA PPA E SOURCE
clear
echo "SOURCE ADDED ----------------------"
echo "PPA ADDED -------------------------"
echo "INSTALLING APPS -------------------"
sudo apt install telegram -y
sudo apt install syncthing -y
sudo apt install opera-stable -y
#sudo apt install skypeforlinux -y


# VARIE
sudo apt install neofetch -y

#INSTALLAZIONI DEV
sudo apt install codium -y
sudo apt install geany -y
sudo snap install clion --classic
sudo snap install pycharm


#INSTALLAZIONI CTF
pip3 install z3-solver
pip3 install pwntools

#wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh

#cd /tmp
#git clone https://github.com/bkerler/ghidra_installer
#./install-ghidra.sh
