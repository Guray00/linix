#!/bin/bash

if [ -e ".log" ]
then
	rm .log
fi


#probe os here
apt -v >>.log 2>&1
if [ $? -eq 0 ]
then
	DISTRO=DEBIAN
fi
pacman -V >>.log 2>&1
if [ $? -eq 0 ]
then
	DISTRO=ARCH
fi

echo "Detected system type: " $DISTRO

######

if [ $DISTRO == "DEBIAN" ]
then
	dpkg -s "python3" >>.log 2>&1 
fi
if [ $DISTRO == "ARCH" ]
then
	pacman -Q "python3" >>.log 2>&1
fi


if [ $? -ne 0 ]

then
	echo "Python3 is not installed, installing now..."  
	
		if [ $DISTRO == "DEBIAN" ]
		then
			sudo apt install python3 -y >>.log 2>&1
		fi
		if [ $DISTRO == "ARCH" ]
		then
			yes | sudo pacman -S python3 >>.log 2>&1
		fi

	else
		echo "Python3 is correctly installed"
fi


dpkg -s "python3-pip" >>.log 2>&1 
if [ $? -ne 0 ]

then
	echo "Pip3 is not installed, installing now..."  
	
		if [ $DISTRO == "DEBIAN" ]
		then
			sudo apt install python3-pip -y >>.log 2>&1
		fi
		if [ $DISTRO == "ARCH" ]
		then
			yes | sudo pacman -S python3-pip >>.log 2>&1
		fi
	
	else
		echo "Pip3 is correctly installed"
fi



pip3 install virtualenv >>.log 2>&1

if [ -d ".venv" ]
then
	echo ".venv found"
	source ./.venv/bin/activate >>.log 2>&1
else
	echo ".venv not found, creating now..."
	virtualenv .venv >>.log 2>&1
	source ./.venv/bin/activate >>.log 2>&1
	echo "Updating python .venv..."
	pip3 install -r ./.venv-requirements.txt >>.log 2>&1

	if [ $DISTRO == "DEBIAN" ]
	then
		echo "Installing apt to .venv..."
		apt download python3-apt >>.log 2>&1
		PYTHONAPT=$(find ./ |grep python3-apt) 
		dpkg-deb -xv $PYTHONAPT ./ >>.log 2>&1
		rm $PYTHONAPT >>.log 2>&1
		cp ./usr/lib/python3/dist-packages ./.venv/lib/python3.6/ -r >>.log 2>&1
		rm -rd ./usr >>.log 2>&1
		
	fi
	if [ $DISTRO == "ARCH" ]
	then
		echo "Installing pacman to .venv..."
		pip3 install python-pacman >>.log 2>&1
	fi
fi


clear
python3 ./scripts/interface.py --distro $DISTRO


deactivate >>.log 2>&1

#uncomment to clear .venv at exit
#rm -rd ./.venv
