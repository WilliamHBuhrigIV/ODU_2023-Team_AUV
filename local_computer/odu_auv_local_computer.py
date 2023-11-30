import time
import math
import RPi.GPIO as GPIO
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
    #motor1.ChangeDutyCycle(motor_duty_cycle)
    #motor1.ChangeFrequency(620)
    #time.sleep(1)
    #motor1.ChangeFrequency(666)
    while True:
        print('Yes?')
        time.sleep(1/motor_max_update_rate)
except KeyboardInterrupt:
    pass
motor1.stop()
motor2.stop()
motor3.stop()
motor4.stop()
GPIO.cleanup()
