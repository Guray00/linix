#!/bin/bash




dpkg -s "python3" &> /dev/null  

if [ $? -ne 0 ]

then
	echo "Python3 is not installed"  
	sudo apt install python3 -y
	
	else
		echo "Python3 is correctly installed"
fi


dpkg -s "python3-pip" &> /dev/null  
if [ $? -ne 0 ]

then
	echo "Pip3 is not installed"  
	sudo apt install python3 -y
	
	else
		echo "Pip3 is correctly installed"
fi


#sudo apt install python3
pip3 install virtualenv

source ./linix_venv/bin/activate

#needed only for dev
#pip3 install -r ./linix_venv/requirements.txt

clear
python3 ./scripts/interface.py

deactivate