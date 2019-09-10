#import rospy
import serial
import time
#from std_msgs.msg import Bool

port="/dev/ttyACM0"
ser=serial.Serial(port,9600)
ser.flushInput
status = 0
class fridge_control:
    def open_fridge(self):
        global status
        while True:
            if status!=1:
                print('a')
                try:
                    ser.write(b'1')
                    print("send open command success")
                    print("Waiting for response...")
                    while True:
                        try:
                            if ser.inWaiting()>0:
                                status=1
                                print("Openning the fridge")
                                break
                                time.sleep(0.1)
                        except:
                            count=count+1
                            if count>=100:
                                count=0
                                print("No response from Arduino")
                                break
                            else:
                                time.sleep(0.1)
                                pass
                    break
                except:
                    print("send error1")
                    time.sleep(0.1)
                    pass
            else:
                print("The fridge is already opened")

    def close_fridge(self):
        global status
        while True:
            if status !=2:
                print('b')
                try:
                    ser.write(b'2')
                    print("send close command success")
                    print("Waiting for response...")
                    while True:
                        try:
                            if ser.inWaiting()>0:
                                status=2
                                print("Closing the fridge")
                                break
                                time.sleep(0.1)
                        except:
                            count=count+1
                            if count>=100:
                                count=0
                                print("No response from Arduino")
                                break
                            else:
                                time.sleep(0.1)
                                pass
                    break
                except:
                    print("send error2")
                    time.sleep(0.1)
                    pass
            else:
                print ("The fridge is already closed")

while True:
    fridge = fridge_control()
    a=input()
    print("you entered", a)
    try:
        if a=='1':
            print("a==1")
            fridge.open_fridge()
        elif a=='2':
            print("a==2")
            fridge.close_fridge()
        else:
            print("Unknown command")
    except:
        pass


    
        
        
    
