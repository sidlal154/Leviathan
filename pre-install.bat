@ECHO OFF
:: batch file for installing external python libraries on windows. User pre-install.sh for non-windows OS
ECHO Starting Initial installation

pip3 install pyyaml
pip3 install requests
pip3 install win10toast

ECHO Installation complete
PAUSE