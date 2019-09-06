import serial
port="/dev/ttyACM0"
ser=serial.Serial(port,9600)
ser.flushInput

while True:
    if ser.inWaiting()>0:
        data=ser.read()
        print(ord(data))
        

