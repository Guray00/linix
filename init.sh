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

pip3 install clint
pip3 instaln PyInquirer


clear
python3 ./scripts/interface.py
