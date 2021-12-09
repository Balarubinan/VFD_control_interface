import smbus
import time
def get_current_value():
    pass

def calculate_alttitude_values():
    pass

addr=0x48
A0=0x40
bus = smbus.SMBus(1)
bus.write_byte(addr, A0)
def measure_voltage():
    # while True:
    value = bus.read_byte(addr)
    print(value)
    return value

# measure_voltage()