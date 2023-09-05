import socket
from socket import SOCK_DGRAM
import time

class Client:

    def __init__(self, HOST="127.0.0.1", PORT=9078):
        self.s = socket.socket(type=SOCK_DGRAM)
        self.s.connect((HOST, PORT))
        self.HOST = HOST
        self.PORT = PORT

    def send_message(self, message):
        self.s.send(str(message).encode())
        # self.s.sendto(str(message).encode(), (self.HOST, self.PORT))


client = Client()

while True:
    client.send_message(
        str(
            [
                cs.ch1out,
                cs.ch2out,
                cs.ch3out,
                cs.ch4out,
                cs.ch5out,
                cs.ch6out,
                cs.ch7out,
                cs.ch8out,
                cs.ch9out,
                cs.ch10out,
                cs.ch11out,
                cs.ch12out
                ]
            )
        )
    # time.sleep(0.1)