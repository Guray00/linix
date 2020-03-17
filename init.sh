#!/bin/bash


echo ""
echo ""

echo "========================================================================"
echo "========================================================================"
echo "                   _       _____  _   _  _____ __   __                  "
echo "                  | |     |_   _|| \ | ||_   _|\ \ / /                  "
echo "                  | |       | |  |  \| |  | |   \ V /                   "
echo "                  | |       | |  |     |  | |    > <                    "
echo "                  | |____  _| |_ | |\  | _| |_  / . \                   "
echo "                  |______||_____||_| \_||_____|/_/ \_\                  "
echo "                                                                        "     
echo "========================================================================"
echo "========================================================================"

echo ""
echo ""



read -p "Hi, are you using debian-based distro? (Ubuntu, Mint, Deppin etc..) [y/n] " so

if [[ "$so" == "y" ]]; then
     read -p "Do you want to install dev-tools? [y/n] " dtools
     
     if [[ "$dtools" == "y" ]]; then
        echo "ok"
     else
        echo "Strings are not equal."
     fi
     

else
    echo "Strings are not equal."
fi
