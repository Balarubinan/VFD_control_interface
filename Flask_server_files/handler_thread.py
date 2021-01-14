import time
def standby_tracker(app):
    global zero_count,standing_by,standby_timeout,pulse_read,pulse_values
    while(True):
        zero_count=(0 if pulse_read else zero_count+1)
        pulse_read = False
        pulse_values.append((0 if zero_count>0 else 1))
        app.logger.error(pulse_values)
        if len(pulse_values)>100:
        #     write_to_rotary(pulse_values)
            pulse_read=[]
        if zero_count==standby_timeout:
            standing_by=True
            return
        print("pulse read is ",pulse_read)
        time.sleep(1)
