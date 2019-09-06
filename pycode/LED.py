import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
print('a')

while True:
    print('b')
    time.sleep(0.1)
    if GPIO.input(25):
        GPIO.output(18,False)
        print(1)
    else:
        GPIO.output(18,True)
        print(2)
        
