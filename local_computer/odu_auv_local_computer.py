import time
import RPi.GPIO as GPIO
#import wiringpi
#wiringpi.wiringPiSetup()
#serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
GPIO.setmode(GPIO.BOARD)
motor1_gpio = 11             #pin
motor2_gpio = 13             #pin
motor3_gpio = 15             #pin
motor4_gpio = 16             #pin
startup_duty_cycle = 50      #%
startup_motor_PWM_Hz = 667  #hz 661-672 are Zero thrust
#motor_duty_cycle = 50       #%
motor_max_update_rate = 400 #hz
GPIO.setup(motor1_gpio, GPIO.OUT)
GPIO.setup(motor2_gpio, GPIO.OUT)
GPIO.setup(motor3_gpio, GPIO.OUT)
GPIO.setup(motor4_gpio, GPIO.OUT)
motor1 = GPIO.PWM(motor1_gpio, startup_motor_PWM_Hz)
motor2 = GPIO.PWM(motor2_gpio, startup_motor_PWM_Hz)
motor3 = GPIO.PWM(motor3_gpio, startup_motor_PWM_Hz)
motor4 = GPIO.PWM(motor4_gpio, startup_motor_PWM_Hz)
motor1.start(startup_duty_cycle)
motor2.start(startup_duty_cycle)
motor3.start(startup_duty_cycle)
motor4.start(startup_duty_cycle)
time.sleep(1)
motor1.ChangeFrequency(620)
motor2.ChangeFrequency(620)
motor3.ChangeFrequency(620)
motor4.ChangeFrequency(620)
time.sleep(1)
motor1.ChangeFrequency(666)
motor2.ChangeFrequency(666)
motor3.ChangeFrequency(666)
motor4.ChangeFrequency(666)
try:
    #motor1.ChangeDutyCycle(motor_duty_cycle)
    #motor1.ChangeFrequency(620)
    #time.sleep(1)
    #motor1.ChangeFrequency(666)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
motor1.stop()
motor2.stop()
motor3.stop()
motor4.stop()
GPIO.cleanup()
