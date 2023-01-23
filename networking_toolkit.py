import nmap
import socket
import requests
import speedtest
from pythonping import ping

# Speed test
class SpeedTest:
    """
    Class used to measure download and upload speed in mbps.
    """
    # Initial Speedtest object from speedtest module
    def __init__(self):
        self.speed_test = speedtest.Speedtest()

    # Returns download speed in mbps
    def download_speed(self):
        return self.convert_bytes_to_mb(self.speed_test.download())
    
    # Returns upload speed in mbps
    def upload_speed(self):
        return self.convert_bytes_to_mb(self.speed_test.upload())

    # Converts bytes to mb 
    def convert_bytes_to_mb(self,bytes):
        KB = 1024
        MB = KB * 1024
        return int(bytes/MB)

# Ping IP
class PingIP:
    """
    Class used to ping inputted IP.
    """
    # Initial ping object
    def __init__(self, ipInput):
        self.ipInput = ipInput
        try:
            socket.inet_aton(ipInput)
        except socket.error:
            print(f"{self.ipInput} is not a valid IP address!")

    # Pings inputted IP
    def ping_ip(self):
        # Asks uer to enter the number of pings
        self.number_of_pings = int(input("Enter the number of pings to send: "))
        try:
            ping(self.ipInput, verbose=True, count=self.number_of_pings) # Pings the IP
        except:
            print(f"{self.ipInput} is not reachable!")

class PortScanner:
    """
    Class used to scan the ports of the inputted IP.
    """
    def __init__(self, ipInput2):
        self.ipInput2 = None
        try:
            socket.inet_aton(ipInput2)
            self.ipInput2 = ipInput2
        except socket.error:
            print(f"{ipInput2} is not a valid IP address!")
            
    # Scans inputted IP
    def port_scanner(self):
        if self.ipInput2:
            ip_address = self.ipInput2
            begin = 1
            end = 1000
            scanner = nmap.PortScanner()
            for i in range(begin,end+1):
                try:
                    res = scanner.scan(ip_address,str(i))
                    res = res['scan'][ip_address]['tcp'][i]['state']
                    print(f"Port {i} is {res}.")
                except KeyError:
                    print(f"{ip_address} is not reachable!")
        else:
            print("IP address is not valid!")

    # Scans specific port of inputted IP
    def specific_port_scanner(self, port):
        if self.ipInput2:
            if port.isnumeric() and (1<=int(port)<=65535):
                ip_address = self.ipInput2
                port = int(port)
                scanner = nmap.PortScanner()
                try:
                    res = scanner.scan(ip_address,str(port))
                    res = res['scan'][ip_address]['tcp'][port]['state']
                    print(f"Port {port} is {res}.")
                except KeyError:
                    print(f"An error occured while scanning the IP {ip_address} of the port {port} may be closed!")
            else:
                print("Invalid port number! Port should be a number between 1 and 65535.")

# User choice
def user_choice():
    while True:
        print("0) Exit \n1) Speedtest \n2) IP ping \n3) Scan Ports of Current IP \n4) Scan Ports of Inputted IP \n5) Scan Specific Port with Inputted IP")
        user_choice = input("Option: ")
        if user_choice == "1":
            url = 'http://www.google.com/'
            try:
                # Check if internet connection is available
                _ = requests.get(url, timeout=5)
                speed_test_obj = SpeedTest()
                download_speed = speed_test_obj.download_speed()
                upload_speed = speed_test_obj.upload_speed()
                if download_speed and upload_speed:
                    print(f"Download: {download_speed} Mbps")
                    print(f"Upload: {upload_speed} Mbps")
            except requests.ConnectionError:
                print("You are not connected to the internet!")
        elif user_choice == "2":
            ipInput = input("Enter IP to ping: ")
            ping_ip_obj = PingIP(ipInput)
            ping_ip_obj.ping_ip()
        elif user_choice == "3":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            PortScanner(ip_address).port_scanner()
        elif user_choice == "4":
            ipInput2 = input("Enter IP to scan: ")
            PortScanner(ipInput2).port_scanner()
        elif user_choice == "5":
            ipInput3 = input("Enter IP to scan: ")
            portInput = input("Enter Port to scan: ")
            PortScanner(ipInput3).specific_port_scanner(portInput)
        elif user_choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    user_choice()