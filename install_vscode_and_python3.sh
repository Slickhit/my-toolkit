#!/bin/bash

# This script downloads and installs Visual Studio Code and Python 3 on a Ubuntu-based Linux system

# Download and install Visual Studio Code
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt-get update
sudo apt-get install code

# Download and install Python 3
sudo apt-get install python3 python3-pip

# Output a message indicating completion of the script
echo "Visual Studio Code and Python 3 are now installed"
