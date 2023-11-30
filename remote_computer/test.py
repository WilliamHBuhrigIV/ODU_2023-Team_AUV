import socket
import time
motor_max_update_rate = 400 #hz
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(1)
try:
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        while True:
            clientsocket.send(bytes(str(1),"utf-8"))
            time.sleep(1/motor_max_update_rate)
except KeyboardInterrupt:
    pass