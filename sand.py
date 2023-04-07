import socket
import binascii
import base64


import time

time.sleep(5)

server_address = ('192.168.10.110', 4001)
print ('connecting to %s port %s' % server_address )

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

sock.send(b'\x23\x03\x53\x00\x79')  #idling on
print('sent idling on')
answer_serv = sock.recv(1024)
print(answer_serv)
time.sleep(5)

sock.send(b'\x23\x03\x73\x00\x99')   #idling off
print('sent idling off')
answer_serv = sock.recv(1024)
print(answer_serv)

