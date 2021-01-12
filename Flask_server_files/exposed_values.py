
# all these variables are meant to be used for only one class (ie only one device!)
# create IO interface to database and use id keys to create a multiple device support variables!

todos = {}
current_val=0
a=[]
# linear resource

last_val = 0
cnt = 0
captured_values = []
stand_by_value = 0

# VFD  resource

current = 0
freq = 50
voltage = 0

# rotary values

pulse_read = False
pulse_values = []
standing_by=False
zero_count=0
standby_timeout=0
