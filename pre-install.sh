#!/bin/sh
#shell file for installing external python libraries on non-windows OS. User pre-install.bat for non-windows OS
echo "Starting initial installation"

pip3 install requests
pip3 install pyyaml

echo "Installation complete"