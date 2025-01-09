Install docker
Pull latest image joshipranjal/screeni-py
https://hub.docker.com/r/joshipranjal/screeni-py?uuid=7B8B547D-EE21-43ED-877A-4DDFD1B8F1FC 
run the scan
Download the data in csv
run this py file on result csv

What is Screeni-py ?
A Python-based stock screener for NSE, India.
Screenipy is an advanced stock screener to find potential breakout stocks from NSE and tell it's possible breakout values. It also helps to find the stocks which are consolidating and may breakout, or the particular chart patterns that you're looking specifically to make your decisions. Screenipy is totally customizable and it can screen stocks with the settings that you have provided.

How to setup and use Screeni-py with Docker?
Download and Install Docker Desktop with default settings
If you are using windows, update WSL (Windows subsystem for linux) by running wsl --update command in command prompt
Restart your computer after installation
Open Docker Desktop and keep it as it is
Open Command Prompt (Windows) or Terminal (Mac/Linux) and run command docker pull joshipranjal/screeni-py:latest
Once installed, always start screenipy by running this command: docker run -it joshipranjal/screeni-py:latest run_screenipy.sh
