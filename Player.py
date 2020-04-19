from worker import Worker


class Player:

    def __init__(self):
        self.worker = None

    def start(self):
        pass

    def send_file(self, file, host, port):
        self.worker = Worker(file, host, port)
        self.worker.start()

    def wait(self):
        self.worker.join()
