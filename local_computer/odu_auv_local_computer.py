import time
import math
import RPi.GPIO as GPIO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4 = input('What what is the IPv4 Address of the Local Host: ')
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
idealzeroThrustHz = 666 #Ideal Value
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
GPIO.setmode(GPIO.BOARD)
motor1_gpio = 11             #pin
motor2_gpio = 13             #pin
motor3_gpio = 15             #pin
motor4_gpio = 16             #pin
startup_duty_cycle = 50      #%
motor_max_update_rate = 400 #hz
GPIO.setup(motor1_gpio, GPIO.OUT)
GPIO.setup(motor2_gpio, GPIO.OUT)
GPIO.setup(motor3_gpio, GPIO.OUT)
GPIO.setup(motor4_gpio, GPIO.OUT)
motor1 = GPIO.PWM(motor1_gpio, zeroThrustHz)
motor2 = GPIO.PWM(motor2_gpio, zeroThrustHz)
motor3 = GPIO.PWM(motor3_gpio, zeroThrustHz)
motor4 = GPIO.PWM(motor4_gpio, zeroThrustHz)
motor1.start(startup_duty_cycle)
motor2.start(startup_duty_cycle)
motor3.start(startup_duty_cycle)
motor4.start(startup_duty_cycle)
try:
    while True:
        motor1data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor2data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor3data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor4data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        #print("Motor 1: ",motor1data,"Motor 2: ",motor2data,"Motor 3: ",motor3data,"Motor 4: ",motor4data)
        motor1.ChangeFrequency(dutyToPWM(motor1data))
        motor2.ChangeFrequency(dutyToPWM(motor2data))
        motor3.ChangeFrequency(dutyToPWM(motor3data))
        motor4.ChangeFrequency(dutyToPWM(motor4data))
except KeyboardInterrupt:
    pass
motor1.stop()
motor2.stop()
motor3.stop()
motor4.stop()
GPIO.cleanup()
