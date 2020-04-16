import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'hello')
print('client sends')

data = sock.recv(1024)
print('received', data)

sock.close()
print('close client')
