#!/bin/bash
sudo su
echo "Hi, are you using debian-based distro? [y/n]"
read so
if [ $so == "y"]; then
	echo "[ ] Installing git..."
	sudo apt-get install git
	echo "[x] Git installed."
	sudo apt-get install snapd
	echo "Are you using plasma (kde)? [y/n]"
	
	read de
	if [$de == "y"]; then
	fi
fi

