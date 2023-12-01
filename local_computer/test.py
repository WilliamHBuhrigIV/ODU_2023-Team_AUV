import time
import math
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4_default = '10.161.80.254'
ipv4 = input('What what is the IPv4 Address of the Local Host: ')
if ipv4=='localhost':
    s.connect((socket.gethostname(),1234))
else:
    s.connect((ipv4,1234))
def thrustclamp(thrustvalue): #Clamps values between -1 and 1
    if thrustvalue>1:
        return 1
    elif thrustvalue<-1:
        return -1
    return thrustvalue
pwmFrequency = 50.75 #hz
def thrustToDuty(thrustvalue): 
    thrustvalue=(thrustclamp(thrustvalue)+1)/2
    return thrustvalue*5+5
    
max_transmission_frequency = 1000 #hz
try:
    while True:
        motor1 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(max_transmission_frequency*4))
        motor2 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(max_transmission_frequency*4))
        motor3 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(max_transmission_frequency*4))
        motor4 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(max_transmission_frequency*4))
        #print("Motor 1: ",motor1,"Motor 2: ",motor2,"Motor 3: ",motor3,"Motor 4: ",motor4)
        #print("Motor 1: ",thrustToDuty(motor1),"Motor 2: ",thrustToDuty(motor2),"Motor 3: ",thrustToDuty(motor3),"Motor 4: ",thrustToDuty(motor4))
except KeyboardInterrupt:
    pass