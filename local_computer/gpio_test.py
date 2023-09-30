import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_gpio = 11
GPIO.setup(led_gpio,GPIO.OUT)
GPIO.output(led_gpio,True)
time.sleep(1)
GPIO.output(led_gpio,False)
GPIO.cleanup()
