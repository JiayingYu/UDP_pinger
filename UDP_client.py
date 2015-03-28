__author__ = 'jiayingyu'
#<a href="http://pymotw.com/2/socket/udp.html">UDP client and server</a>

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1)

try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping #' + str(i) + " " + time.ctime(start)
        try:
            sent = sock.sendto(message, server_addr)
            print("Sent " + message)
            data, server = sock.recvfrom(4096)
            print("Received " + data)
            end = time.time();
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")
        except socket.timeout:
            print("#" + str(i) + " Time out\n")

finally:
    print("closing socket")
    sock.close()