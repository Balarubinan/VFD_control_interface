import smbus
import time
def get_current_value():
    pass

def calculate_alttitude_values():
    pass

addr=0x48
A0=0x40
bus = smbus.SMBus(1);
bus.write_byte(addr, A0)
def measure_voltage():
    # while True:
    value = bus.read_byte(addr)
    print(value)
    return value

def ready_method():
   # sio.emit('typeUpdate',{"type":"send",'devicename':"RaspiTractor1"})
    # sio.emit('nameReg',{'devicename':"Tractor1"})
    while(1):
        val=measure_voltage()
        print("kdfshgijSending value", val)
        # val={"value":random.randint(-12,12)/51}
        print("Sending value",val/51)
       # sio.emit('valueUpdate',val)
        time.sleep(.5)


#measure_voltage()
ready_method()