#!/bin/python3

import argparse
import time
import socket
import header
import re

#Arguement Parsing for CLI
parser = argparse.ArgumentParser(description='A Simple Network port scanner.')
parser.add_argument('host', help="Ip address of host to scan.")
#parser.add_argument("-v", dest="verboseMode", action='store_true', help="Verbose Mode - Show realtime scanning status.")			Verbose mode for future updates
parser.add_argument("-p", dest="port_range", default="1-1024", help="Port range to scan(Default is 1-1024)")
parser.add_argument("-s", dest="scan", help="Scantype (TCP Scan, UDP Scan or ICMP/Ping Sweep)", choices=["U","T","I"], default = "-sT")
args = parser.parse_args()

target = args.host  #Target IP to scan

#Define Port Range
port_range = args.port_range.split("-")  #Split the input port range into starting and ending port
port_start = int(port_range[0])
port_end = int(port_range[1])
scantype = args.scan

target_name = socket.getfqdn(target)            #Set Target IP Variable
try:
    target_ip = socket.gethostbyname(target)       #Set Target Name Variable
except socket.gaierror:
    print("Invalid host to scan. Please verify that the host you are scanning exists.")
    #quit()

ip_regex = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
hostmatch = re.match(ip_regex, target)
try:
    if hostmatch == True:
        target_ip = socket.getfqdn(target)
        print("ip address")
    else:
        target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid host to scan")
print("Scanning", target_ip, "from port ", port_start ," to ", port_end,".")
print("\n")
if (scantype == "U"):
    sock = socket.SOCK_DGRAM
    stype = "UDP Scan"
elif (scantype == "T"):
	sock = socket.SOCK_STREAM
	stype = "TCP Scan"
else:
    sock = socket.SOCK_STREAM
    stype = "Ping Sweep/ Host Discovery"

scan = socket.socket(socket.AF_INET, sock)

with scan as s:
        def printer(port):
            print("Scanning ", target_ip , " at port", port)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target_ip, port))
            print(result)
            if result ==0:
                print("Port {} is open".format(port))
            else:
                print("Port {} is close".format(port))
            s.close()
#def printer(port):
 #   print("Scanning ", socket.getfqdn(target) , " at port", port)

for x in range(port_start,port_end+1):
    printer(x)

print(stype)