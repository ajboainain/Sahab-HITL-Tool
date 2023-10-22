# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# sock.bind(("0.0.0.0", 5052))

# while True:
#     data, addr = sock.recvfrom(1024)
#     print(str(data))


from pymavlink import mavutil

mav = mavutil.mavlink_connection('udp:localhost:5052')

while True:
    msg = mav.recv_match(type="SERVO_OUTPUT_RAW", blocking=True)

    if  msg:
        print(msg.to_dict())