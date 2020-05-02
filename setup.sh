#! bin/bash
clear
echo -e "                \e[31;1mInstalling SniperMan\e[0m"
echo -e "                \e[34;1mPlease Wait upto 5min\e[0m"
apt-get -y update > /dev/null 2>&1
apt-get -y install git > /dev/null 2>&1
apt-get -y install python3 > /dev/null 2>&1
python3 -m pip install --upgrade pip
pip install tqdm > /dev/null 2>&1
pip install pyfiglet > /dev/null 2>&1
clear
echo -e "\e[1;92m[*]SniperMan is installed To run SniperMan type '\e[93mpython SniperMan.py'\e[0m "
