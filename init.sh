#!/bin/bash

#probe os here
apt -v&>/dev/null
if [ $? -eq 0 ]
then
	DISTRO=DEBIAN
fi
pacman -V&>/dev/null
if [ $? -eq 0 ]
then
	DISTRO=ARCH
fi

echo "Detected system type: " $DISTRO

######

if [ $DISTRO == "DEBIAN" ]
then
	dpkg -s "python3" &> /dev/null 
fi
if [ $DISTRO == "ARCH" ]
then
	pacman -Q "python3" &> /dev/null
fi
 

if [ $? -ne 0 ]

then
	echo "Python3 is not installed, installing now..."  
	
		if [ $DISTRO == "DEBIAN" ]
		then
			sudo apt install python3 -y
		fi
		if [ $DISTRO == "ARCH" ]
		then
			yes | sudo pacman -S python3 
		fi

	else
		echo "Python3 is correctly installed"
fi


dpkg -s "python3-pip" &> /dev/null  
if [ $? -ne 0 ]

then
	echo "Pip3 is not installed, installing now..."  
	
		if [ $DISTRO == "DEBIAN" ]
		then
			sudo apt install python3-pip -y
		fi
		if [ $DISTRO == "ARCH" ]
		then
			yes | sudo pacman -S python3-pip
		fi
	
	else
		echo "Pip3 is correctly installed"
fi


#sudo apt install python3

#error not redirected for trubleshooting
pip3 install virtualenv>/dev/null
source ./linix_venv/bin/activate


echo "Updating python venv..."
pip3 install -r ./linix_venv/requirements.txt >/dev/null

if [ $DISTRO == "DEBIAN" ]
then
	apt download python3-apt > /dev/null
	PYTHONAPT=$(find ./ |grep python3-apt)
	dpkg-deb -xv $PYTHONAPT ./ >/dev/null > /dev/null
	rm $PYTHONAPT
	cp ./usr/lib/python3/dist-packages ./linix_venv/lib/python3.6/ -r
	rm -rd ./usr
fi
if [ $DISTRO == "ARCH" ]
then
	pip3 install python-pacman >/dev/null
fi


clear
python3 ./scripts/interface.py $DISTRO

#ONLY FOR DEV
if [ $DISTRO == "DEBIAN" ]
then

	rm -rd ./linix_venv/lib/python3.6/dist-packages

fi
if [ $DISTRO == "ARCH" ]
then
	pip3 uninstall python-pacman >/dev/null
fi

deactivate
