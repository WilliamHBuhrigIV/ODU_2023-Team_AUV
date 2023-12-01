import time
import math
import socket
import RPi.GPIO as GPIO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4_default = '10.161.80.254'
ipv4 = input('What what is the IPv4 Address of the Local Host: ')
if ipv4=='localhost':
    s.connect((socket.gethostname(),1234))
else:
    s.connect((ipv4,1234))
print('Connection Established with '+ipv4+'!')
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
GPIO.setmode(GPIO.BOARD)
motor1_gpio = 11             #pin
motor2_gpio = 13             #pin
motor3_gpio = 15             #pin
motor4_gpio = 16             #pin
startup_duty_cycle = 7.5      #%
motor_max_update_rate = 16 #hz
GPIO.setup(motor1_gpio, GPIO.OUT)
GPIO.setup(motor2_gpio, GPIO.OUT)
GPIO.setup(motor3_gpio, GPIO.OUT)
GPIO.setup(motor4_gpio, GPIO.OUT)
motor1 = GPIO.PWM(motor1_gpio, pwmFrequency)
motor2 = GPIO.PWM(motor2_gpio, pwmFrequency)
motor3 = GPIO.PWM(motor3_gpio, pwmFrequency)
motor4 = GPIO.PWM(motor4_gpio, pwmFrequency)
motor1.start(startup_duty_cycle)
motor2.start(startup_duty_cycle)
motor3.start(startup_duty_cycle)
motor4.start(startup_duty_cycle)
motor_statup_period = 1 #seconds
print('Motors Initizlizing! Waiting '+motor_statup_period+'second(s)!')
time.sleep(motor_statup_period)
print('Motor Startup Completed Receiving Signals from Remote.')
try:
    while True:
        #s.send(bytes(str('1'),'utf-8'))
        motor1data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor2data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor3data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        motor4data = int(s.recv(32).decode("utf-8"))/1000*2-1
        time.sleep(1/(motor_max_update_rate*4))
        #print("Motor 1: ",motor1data,"Motor 2: ",motor2data,"Motor 3: ",motor3data,"Motor 4: ",motor4data)
        motor1.ChangeDutyCycle(thrustToDuty(motor1data))
        motor2.ChangeDutyCycle(thrustToDuty(motor2data))
        motor3.ChangeDutyCycle(thrustToDuty(motor3data))
        motor4.ChangeDutyCycle(thrustToDuty(motor4data))
except KeyboardInterrupt:
    pass
motor1.stop()
motor2.stop()
motor3.stop()
motor4.stop()
GPIO.cleanup()
s.shutdown(socket.SHUT_RDWR)
s.close()
