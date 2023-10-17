import socket
from socket import SOCK_DGRAM

HOST="127.0.0.1"
PORT=9078
socket = socket.socket()

def attempt_connection():
    while True:
        try: 
            socket.connect((HOST, PORT))
            break
        except:
            continue # try again

while True:
        try:
            data = socket.recv(1024).decode()
            if not data:
                break
            if data == 'ok':
                socket.sendall(str(
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
                ).encode())
        except:
             attempt_connection()
        