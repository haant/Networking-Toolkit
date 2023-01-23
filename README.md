# Networking Toolkit

## About the Project

![CLI-Networking-Script](https://github.com/haant/Networking-Toolkit/blob/main/CLI_networking_script.png)

This script contains several classes that perform various network-related tasks. The SpeedTest class uses the speedtest module to measure the download and upload speed of the user's internet connection in megabits per second (Mbps). The PingIP class allows the user to ping a specific IP address and returns the ping results. The PortScanner class allows the user to scan the ports of a specific IP address, either the current IP or an inputted IP. Additionally, the user can also scan a specific port with an inputted IP address. The script is written in Python and is designed to be easy to use and understand, making it a useful tool for network administrators, developers and anyone who works with networks.

## Getting Started

Please make sure you have the following libraries pre-installed:
```
nmap
speedtest
socket
requests 
pythonping
```
1) To run the script, open the terminal, navigate to the directory where the script is located and type the following command:
```
python3 networking_toolkit.py
```
2) You will be presented with a menu of options. Select the one you wish to use:
```
0) Exit
1) Speedtest
2) IP ping
3) Scan Ports of Current IP
4) Scan Ports of Inputted IP
5) Scan Specific Port with Inputted IP
```
3) For example, if you select option 2, you will be prompted to enter an IP address to ping, as well as the number of pings you would like to send. Once you have entered that information, the script will display the ping results, and re-prompt you for another choice. 
4) If you select option 3, the script will scan the ports of your current IP address. 
5) If you select option 4, you will be prompted to enter an IP address to scan, and the script will scan the ports of the inputted IP address. 
6) If you select option 5, you will be prompted to enter an IP address and port number to scan, and the script will scan the specific port with the inputted IP address. 
7) Once you finish with your selection, the script will display the results of the task you selected. 
Please refer below for the GitHub pages of the above libraries. They can all be installed uisng ```pip```.

## Contact

Please contact me on Twitter [@haant05](https://twitter.com/haant05) or LinkedIn [Denas Zelvys](https://www.linkedin.com/in/denaszelvys/) if you have any additional questions about thie project. 

Many thanks for checking out my project!

-- Denas

## Acknowledgments

All libraries in thie project are as follows:

- [nmap](https://github.com/home-assistant-libs/python-nmap)
- [speedtest](https://github.com/sivel/speedtest-cli)
- [socket](https://docs.python.org/3/library/socket.html)
- [requests](https://github.com/psf/requests)
- [pythonping](https://pypi.org/project/pythonping/)
