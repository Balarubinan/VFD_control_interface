import smbus
import time
def get_current_value():
    pass

def calculate_alttitude_values():
    pass

def measure_voltage():
    addr=0x48
    A0=0x40
    bus = smbus.SMBus(1)
    while True:
        bus.write_byte(addr, A0)
        value = bus.read_byte(addr)
        print(value)
        time.sleep(0.1)

measure_voltage()