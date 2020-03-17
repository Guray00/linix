#!/bin/bash


# AGGIUNTA DELLE PPA PER AVERE I DEB
wget -O - http://deb.opera.com/archive.key | sudo apt-key add -
sudo sh -c 'echo "deb http://deb.opera.com/opera-stable/ stable non-free" >> /etc/apt/sources.list.d/opera.list' 

sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 0xd66b746e
sudo sh -c 'echo "deb http://download.skype.com/linux/repos/debian/ stable non-free" >> /etc/apt/sources.list'

sudo aptitude update 

#INSTALLAZIONI FONDAMENTALI
sudo aptitude install opera
sudo apt install skypeforlinux
sudo apt-get install git -y
sudo apt-get install curl -y


#INSTALLAZIONI DEV
sudo snap install clion -y
sudo snap install pycharm -y
sudo apt-get install geany

#INSTALLAZIONI CTF
cd /tmp
git clone https://github.com/bkerler/ghidra_installer
./install-ghidra.sh

sudo apt-get install pip3 -y

pip3 install z3-solver
pip3 install pwntools

wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh