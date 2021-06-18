#!/bin/python3

import argparse
import time
import socket
import atexit
import welcome

current_time = time.localtime(time.time())
start_time = time.strftime("%H:%M:%S", current_time)
print("  "*35 ,"Started scanning at ", start_time)
parser = argparse.ArgumentParser(description='A Simple Network port scanner.')
parser.add_argument('host', help="Ip address of host to scan.")
#parser.add_argument("-v", dest="verboseMode", action='store_true', help="Verbose Mode - Show realtime scanning status.")			Verbose mode for future updates
parser.add_argument("-p", dest="port_range", default="1-1024", help="Port range to scan(Default is 1-1024)")
parser.add_argument("-s", dest="scan", help="Scantype (TCP Scan, UDP Scan or ICMP/Ping Sweep)", choices=["U","T","I"], default = "-sT")
args = parser.parse_args()

target = args.host  #Target IP to scan
port_range = args.port_range.split("-")  #Split the input port range into starting and ending port
port_start = int(port_range[0])
port_end = int(port_range[1])

hostname = socket.getfqdn(target)
print("Scanning", hostname, "from port ", port_start ," to ", port_end,".")

print(socket.getfqdn(target))
print(socket.gethostbyname(target))
scantype = args.scan

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

def printer(port):
    if args.verboseMode:
    	print("Scanning ", target , " at port", port)

for x in range(port_start,port_end+1):
    printer(x)

print(stype)