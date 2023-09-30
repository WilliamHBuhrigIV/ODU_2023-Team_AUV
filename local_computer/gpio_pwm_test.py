import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
p_gpio = 11
GPIO.setup(p_gpio, GPIO.OUT)
p = GPIO.PWM(p_gpio, 60)
p.start(1)
input('Press return to decrease:')
p.ChangeDutyCycle(0.5)
input('Press return to stop:')
p.stop()
GPIO.cleanup()
