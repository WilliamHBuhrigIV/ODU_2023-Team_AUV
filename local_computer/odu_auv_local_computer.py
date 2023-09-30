import RPi.GPIO as GPIO
import wiringpi
GPIO.setmode(GPIO.BOARD)
motor1_gpio = 4
motor2_gpio = 13
motor3_gpio = 14
motor4_gpio = 27
GPIO.setup(motor1_gpio, GPIO.OUT)
GPIO.setup(motor2_gpio, GPIO.OUT)
GPIO.setup(motor3_gpio, GPIO.OUT)
GPIO.setup(motor4_gpio, GPIO.OUT)
motor1 = GPIO.PWM(motor1_gpio, 60)
motor2 = GPIO.PWM(motor2_gpio, 60)
motor3 = GPIO.PWM(motor3_gpio, 60)
motor4 = GPIO.PWM(motor4_gpio, 60)
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
GPIO.cleanup()