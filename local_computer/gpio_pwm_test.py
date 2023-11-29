import time
#import RPi.GPIO as GPIO
frequency = 500
duty = 0.5
GPIO.setmode(GPIO.BOARD)
p_gpio = 11
GPIO.setup(p_gpio, GPIO.OUT)
p = GPIO.PWM(p_gpio, frequency)
p.start(0.5)
print('Duty Cycle set at '+str(duty*100)+'%.')
try:
    while True:
        frequency = input('Select a Frequency to Test:')
        print('Currently Testing at '+str(frequency)+'hz.')
        p.ChangeFrequency(frequency)
except KeyboardInterrupt:
    pass
print('\nEnding Session at '+str(frequency)+'hz.')
p.stop()
GPIO.cleanup()