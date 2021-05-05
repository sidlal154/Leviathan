# Leviathan

A simple python script to alert user for vaccine slots. This code searches for given number of available vaccine capacity sessions in a district every 5 seconds, and if present dumps out the details in a file named ```available-centers.yaml``` with a pop-up alert. (TODO: Alers are currently only supported on windows 10, add support for other OS as well)

# Prerequisites:

1) Python 3.4+ : For installation https://www.python.org/downloads/
2) Downloan pip/pip3: 
    - pip should be automatically installed with Python 3.4+. To check, run ```pip help``` or ```pip3 help``` in command prompt/Powershell/Terminal
    - If not present, follow this tutorial: https://phoenixnap.com/kb/install-pip-windows
3) Run ```pre-install.bat``` for Windows OS, ```pre-install.sh``` for non-windows OS (Ubuntu, Mac, etc) for installation of some python external libraries


# How to Run

Use ```main.py``` to run the script which searches for available vaccine slots in your district, with the help of the following flags:
  - ```--distname``` : name of your district (Deafult: BBMP)
  - ```--state```: name of your state (Default: Karnataka)
  - ```--age```: minimum age group (18/45) (Default: 18)
  - ```--cap```: minimum number of available vaccine capacity you want in your session (Default: 1)(for eg. if searching for multiple people)
  - ```-h``` or ```--help```: for help

Usage example: If you are living in BBMP, Karnataka, and are 18-44 age group, and are looking for vaccine session slots for 3 people together, your command should be ```python main.py --distname BBMP --state Karnataka --age 18 --cap 3``` (Windows) or ```python3 main.py --distname BBMP --state Karnataka --age 18 --cap 3``` (Non-Windows)

Aternatively, if already know the district id of your district, by running ```python fetchdistid.py <District Name> <State Name>``` then use ```--distid``` flag instead of ```--distname``` and ```--state``` flags.


# Important

As per https://apisetu.gov.in/public/marketplace/api/cowin, only 100 API calls are allowed in 5 min from 1 IP. Please keep this in mind while tuning the rate of API calls, since it may cause your IP to be blocked. Our rate is currently 60 API calls in 5 min which is safe.
