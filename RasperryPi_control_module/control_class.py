import RPi.GPIO as GPIO
import gpiozero as gpz
from .analog_read import analog_read
from time import sleep
from requests import get,put,post
import time
from threading import Thread

class ControlModule():
    # here gndPin is the analog circuit pin -> b_pin
    def __init__(self,linear=11,rotary=12,vfd=13,gndPin=14):
        self.linPin=linear
        self.rotPin=rotary
        self.vfdPin=vfd
        self.gndPin=gndPin
        self.running=True
        # self.threads=[]
        self.start_up_operations()
        # timeout is in seconds
        self.standby_timeout=15

    def in_standby(self):
        pass

    def start_up_operations(self):
        for x in [self.send_linear_value,self.send_rotary_value]:
            t=Thread(target=x)
            t.start()
            # self.threads.append(t)
        print("Startup operations complete!!")


    def send_linear_value(self):
        while(self.running):
            val=analog_read(self.linPin,self.gndPin)
            print("Value read for linear : ",val)
            post(f"http://balarubinan.pythonanywhere.com/lin/{val}")
            time.sleep(0.8)

    def send_rotary_value(self):
        while(self.running):
            val=GPIO.input(self.rotPin)
            # print("Value read for linear : ", val)
            # check if high works or else use a 1
            if val==GPIO.HIGH:
                # post command takes a micro second or 2 hence wait time is produced
                # we cannot wait in here if we wait in here then we may miss rotary encoder pulses
                # use a thread or a async statment to get rid of instantaneous wait time!
                post(f"http://Balarubinan.pythonanywhere.com/rot/{val}")

    def kill_sensors(self,secs):
        self.running=False
        print("All threads have been killed stopped")


# start the program
ControlModule()





