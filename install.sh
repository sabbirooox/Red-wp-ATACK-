#!/bin/bash
clear
echo -e "\e[1;32m[+] Installing Requirements...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python -y
pip install colorama

echo -e "\e[1;32m[+] Downloading RED TOOLS...\e[0m"
# নিচের লাইনে আপনার গিটহাবের সঠিক লিংক বসান
curl -sL https://raw.githubusercontent.com/sabbiroox/YOUR-REPO-NAME/main/red_tools.py -o red_tools.py

chmod +x red_tools.py

echo -e "\e[1;34m[✓] Installation Complete!\e[0m"
echo -e "\e[1;33mType 'python red_tools.py' to run the tool.\e[0m"
