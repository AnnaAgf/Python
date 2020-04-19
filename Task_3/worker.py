from scapy.all import *


class Worker(threading.Thread):
    def __init__(self, file, host, port):
        threading.Thread.__init__(self)
        self.file = file
        self.host = host
        self.port = port
        self.payload = None

    def run(self):
        sock = socket.socket()
        sock.connect((self.host, int(self.port)))

        packets = rdpcap(self.file)
        for i in range(len(packets)):
            self.payload = packets[i].payload
            if i == 0:
                pass
            else:
                interval = packets[i].time - packets[i - 1].time
                time.sleep(interval)
            sock.send(bytes(self.payload))

        sock.close()
