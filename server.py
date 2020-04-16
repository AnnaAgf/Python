import getopt
import socket
import sys

print('hfuck1')
host = None
port = None
try:
    options, args = getopt.getopt(
        sys.argv[1:], "h:p:",
        ["host=", "port="])
    for name, value in options:
        if name in ('-h', '--host'):
            host = value
        if name in ('-p', '--port'):
            port = value
except getopt.GetoptError as err:
    print(str(err))
    sys.exit(1)

print(host, port)
sock = socket.socket()
sock.bind((host, int(port)))
sock.listen()
print('fuck3')
while True:
    try:
        soc, address = sock.accept()
    except socket.error:
        pass
    else:
        print('Connected by', address)
        data = soc.recv(1024)
        print('RECEIVED FROM CLIENT', address)
        if not data:
            break
        soc.sendall(data.upper())
