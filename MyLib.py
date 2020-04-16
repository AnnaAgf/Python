import socket

class MyLib:

    def hello(self, name):
        print("Hello, %s!" % name)

    def start(self, host, port):
        sock = socket.socket()
        sock.connect((host, port))
        return sock

    def send_file(self, message):
        sock.send(b'hello')