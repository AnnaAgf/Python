import getopt
import logging
import socket
import sys


class Server:
    host = None
    port = None
    sock = None

    def __init__(self):
        self.host = self.host
        self.port = self.port
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    def parse_cmd(self):
        try:
            options, args = getopt.getopt(
                sys.argv[1:], "h:p:",
                ["host=", "port="])
            for name, value in options:
                if name in ('-h', '--host'):
                    self.host = value
                if name in ('-p', '--port'):
                    self.port = value
        except getopt.GetoptError as err:
            print(str(err))
            sys.exit(1)

    def start_server(self):
        self.sock = socket.socket()
        self.sock.bind((self.host, int(self.port)))
        self.sock.listen()
        self.logger.info('Server starts listen')

    def serve(self):
        while True:
            try:
                soc, address = self.sock.accept()
            except socket.error:
                pass
            else:
                self.logger.info('Client established connection')
                data = soc.recv(10000)
                self.logger.info('Received data from client')
                if not data:
                    break

    def stop_server(self):
        self.sock.close()
        self.logger.info('Server stops')


if __name__ == '__main__':
    server = Server()
    server.parse_cmd()
    server.start_server()
    server.serve()
    server.stop_server()
