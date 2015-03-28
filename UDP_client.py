__author__ = 'jiayingyu'
#<a href="http://pymotw.com/2/socket/udp.html">UDP client and server</a>

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
message = "Ping #1 time"
try:
    print("sending " + message)
    sent = sock.sendto(message, server_addr)
    data, server = sock.recvfrom(4096)
    print("received " + data)
finally:
    print("closing socket")
    sock.close()