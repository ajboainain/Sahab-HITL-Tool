import socket
from socket import SOCK_DGRAM
import time

class Client:

    def __init__(self, HOST="127.0.0.1", PORT=9077):
        self.s = socket.socket(type=SOCK_DGRAM)
        self.HOST = HOST
        self.PORT = PORT

    def send_message(self, message):
        self.s.sendto(str(message).encode(), (self.HOST, self.PORT))


client = Client()

while True:
    output = [
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
                cs.ch12out,
                ]
    # print(output)
    client.send_message(str(output))
    time.sleep(0.2)