#!/bin/bash
clear
echo -e "                \e[31;1mInstalling SniperMan\e[0m"
echo -e "                \e[34;1mPlease Wait upto 5min\e[0m"
apt-get -y install python-pip > /dev/null 2>&1
apt-get -y install python3-pip > /dev/null 2>&1
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip install tqdm > /dev/null 2>&1
pip install pyfiglet==0.7 > /dev/null 2>&1
clear
echo -e "\e[1;92m[*]SniperMan is installed To run SniperMan type '\e[93mpython3 SniperMan.py'\e[0m "
