import socket
import threading


class MyThread(threading.Thread):
    def __init__(self, file, host, port):
        threading.Thread.__init__(self)
        self.file = file
        self.host = host
        self.port = port

    def run(self):
        sock = socket.socket()
        sock.connect((self.host, int(self.port)))
        print('client connects')
        for i in range(0, 4):
            sock.send(bytes(self.file))
            print('client sends', i)


class MyLib:
    mythread = None

    def hello(self, name):
        print("Hello, %s!" % name)

    def start(self):
        pass

    def send_file(self, file, host, port):
        self.mythread = MyThread(file, host, port)
        self.mythread.start()
        print('client sends from thread')

    def wait(self):
        self.mythread.join()
        print('stop thread')


# if __name__ == '__main__':
#     a = MyLib()
#     a.send_file('hello', 'localhost', 9090)
#     a.wait()