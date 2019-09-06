import serial
import time
port="/dev/ttyACM1"
ser=serial.Serial(port,9600)
ser.flushInput

while True:
    a=input()
    print("you entered", a)
    try:
        if a=='1':
            print(1)
            ser.write(b'1')
            print("send 1 success")
            time.sleep(0.1)
        elif a=='2':
            print(2)
            ser.write(b'2')
            print("send 2 success")
        else:
            
            print("Unknow command")   
    except:
        print("send error")
        time.sleep(0.1)
        pass
ser.close()
    


        

