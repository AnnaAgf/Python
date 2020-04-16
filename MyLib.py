import socket
import threading


class MyLib:
    a = 4

    def hello(self, name):
        print("Hello, %s!" % name)

    def start(self):
        pass

    def send_file(self, msg, host, port):
        sock = socket.socket()
        sock.connect((host, int(port)))
        print('client connects')
        for i in range (0, 4):
            sock.send(msg)
            print('client sends', i)
        self.a = self.a + 1

    def wait(self):
        print(self.a)
        pass