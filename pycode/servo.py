import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(flickSensor,GPIO.IN)
GPIO.setup(outputPins,GPIO.OUT)