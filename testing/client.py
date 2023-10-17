import socket

# Define the server address and port
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8000

# Define the message to send
MESSAGE = 'hello'

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Wait for the server to send "ok"
while True:
    response = client_socket.recv(1024).decode()
    if response == 'ok':
        break

# Send the message
client_socket.send(MESSAGE.encode())

# Close the socket
client_socket.close()
