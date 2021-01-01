import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# # define GPIO pins with variables a_pin and b_pin
# a_pin = 18
# b_pin = 23


# create discharge function for reading capacitor data
def discharge(a_pin,b_pin):
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)


# create time function for capturing analog count value
def charge_time(a_pin,b_pin):
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count + 1
    return count


# create analog read function for reading charging and discharging data
def analog_read(pin1,pin2):
    discharge(pin1,pin2)
    return charge_time(pin1,pin2)


# provide a loop to display analog data count value on the screen
# while True:
#     print(analog_read())
#     time.sleep(1)
