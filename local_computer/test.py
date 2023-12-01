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
parameterA = 0.444970796979893
parameterB = 1.15066476381101
parameterC = -140
parameterD = -243
idealzeroThrustHz = 666 #hz Ideal Value
def pwmShift(expectedPWMValue): #Provides Adjusted Value from Theoretical
    return parameterA*math.pow(expectedPWMValue,parameterB)
zeroThrustHz=pwmShift(idealzeroThrustHz)
def dutyToPWM(thrustvalue): 
    thrustvalue=thrustclamp(thrustvalue)
    if thrustvalue>0:
        return pwmShift(parameterC*thrustvalue+idealzeroThrustHz)
    elif thrustvalue<-0:
        return pwmShift(parameterD*thrustvalue+idealzeroThrustHz)
    return zeroThrustHz
motor_max_update_rate = 400 #hz
try:
    while True:
        motor1 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor2 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor3 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor4 = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        print("Motor 1: ",motor1,"Motor 2: ",motor2,"Motor 3: ",motor3,"Motor 4: ",motor4)
        
except KeyboardInterrupt:
    pass