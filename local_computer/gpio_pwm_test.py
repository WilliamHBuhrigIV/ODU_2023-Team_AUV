import time
import RPi.GPIO as GPIO
frequency = 500
duty = 0.5
GPIO.setmode(GPIO.BOARD)
p_gpio = 11
GPIO.setup(p_gpio, GPIO.OUT)
p = GPIO.PWM(p_gpio, frequency)
p.start(duty)
print('Duty Cycle set at '+str(duty*100)+'%.')
try:
    print('Currently Testing at 500 hz.')
    p.ChangeFrequency(500)
    input('Press Return to Test Next Frequency')
    print('Currently Testing at 583 hz.')
    p.ChangeFrequency(583)
    input('Press Return to Test Next Frequency')
    print('Currently Testing at 666 hz.')
    p.ChangeFrequency(666)
    input('Press Return to Test Next Frequency')
    print('Currently Testing at 783 hz.')
    p.ChangeFrequency(783)
    input('Press Return to Test Next Frequency')
    print('Currently Testing at 900 hz.')
    p.ChangeFrequency(900)
    input('Press Return to Stop')
    print('500 Hz Frequency Test with Shift.')
    p.ChangeFrequency(0.7444*500+78.046)
except KeyboardInterrupt:
    pass
print('\nEnding Session at '+str(frequency)+'hz.')
p.stop()
GPIO.cleanup()
