import socket

s = socket.socket()

s.connect(('localhost', 8080))
print(s.recv(1024))
s.send(b'Hello world!')
s.close()