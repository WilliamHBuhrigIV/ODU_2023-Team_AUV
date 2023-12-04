import time
import math
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def thrustclamp(thrustvalue): #Clamps values between -1 and 1
    if thrustvalue>1:
        return 1
    elif thrustvalue<-1:
        return -1
    return thrustvalue
def thrustToDuty(thrustvalue): 
    thrustvalue=(thrustclamp(thrustvalue)+1)/2
    return thrustvalue*5+5
ipv4_default = '10.161.80.254'
ipv4 = input('What what is the IPv4 Address of the Local Host: ')    
max_transmission_frequency = 100 #hz
pwmFrequency = 50.75 #hz
if ipv4=='localhost':
    s.connect((socket.gethostname(),1234))
else:
    s.connect((ipv4,1234))
try:
    while True:
        #motor1 = int(s.recv(32).decode("utf-8"))/1000*2-1
        #time.sleep(1/(max_transmission_frequency*4))
        #motor2 = int(s.recv(32).decode("utf-8"))/1000*2-1
        #time.sleep(1/(max_transmission_frequency*4))
        #motor3 = int(s.recv(32).decode("utf-8"))/1000*2-1
        #time.sleep(1/(max_transmission_frequency*4))
        #motor4 = int(s.recv(32).decode("utf-8"))/1000*2-1
        #time.sleep(1/(max_transmission_frequency*4))
        
        rawmotordata = s.recv(32).decode("utf-8")
        print(rawmotordata)
        motordata = int(rawmotordata)
        print(motordata)
        motor4 = int(motordata % 1000)
        motor3 = int((motordata % 1000000 - motor4)/1000)
        motor2 = int((motordata % 1000000000 - (motor3+motor4))/1000000)
        motor1 = int((motordata % 1000000000000 - (motor4+motor2+motor3))/1000000000)
        #print("Motor 1: ",motor1,"Motor 2: ",motor2,"Motor 3: ",motor3,"Motor 4: ",motor4)
        thrust4 = thrustclamp((motor4-500)/1000)
        thrust3 = thrustclamp((motor3-500)/1000)
        thrust2 = thrustclamp((motor2-500)/1000)
        thrust1 = thrustclamp((motor1-500)/1000)
        #print("Motor 1: ",thrust1,"Motor 2: ",thrust2,"Motor 3: ",thrust3,"Motor 4: ",thrust4)
        time.sleep(1/(max_transmission_frequency))

        #print("Motor 1: ",motor1,"Motor 2: ",motor2,"Motor 3: ",motor3,"Motor 4: ",motor4)
        #print("Motor 1: ",thrustToDuty(motor1),"Motor 2: ",thrustToDuty(motor2),"Motor 3: ",thrustToDuty(motor3),"Motor 4: ",thrustToDuty(motor4))
except KeyboardInterrupt:
    pass
s.shutdown(socket.SHUT_RDWR)
s.close()