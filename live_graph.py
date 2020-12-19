import numpy as np
import matplotlib.pyplot as plt
from random import randint
import time
from reader import yielder

# plt.axis([0, 100, 0, 1])
# plt,axis=plt1.subplots()
plt.grid(True)

# graph axis outruns data after certain time...fix that
# create a whole application window



seconds = 0
values_to_show = 0
wait_time = 0
treshold = 0


def init_settings():
    global values_to_show, wait_time,treshold
    # define additional settings from console
    values_to_show = 20
    wait_time = 1
    treshold=30


def get_data():
    """simulator of reading values from the board"""
    # if randint(1, 100) % 2 == 0:
    #     return False, -1
    # return True, np.random.random()
    return True,yielder()


def kill_graph():
    pass
    # add hardware interuppt code to kill the running graph


def add_point():
    global seconds
    current_reading = 0
    times, vals = [0], []
    ind = 1
    while (True):
        value_read, reading = get_data()
        if (value_read):
            current_reading = reading
            vals.append(current_reading)
            if seconds*wait_time > 20:
                # plt.plot(times[ind:], vals[ind:],color="blue")
                # plotting only the last values_to_show number of  values using list slicing
                # plt.axis([ind, values_to_show + ind - 1, 0, 1])
                plt.axis([times[ind], times[values_to_show + ind - 1], 0, 100])
                # plt.fill_between(x, y)
                ind += 1

            plt.stackplot(times, vals, color=("blue" if current_reading>treshold else "red"))
            plt.pause(0.05)
        else:
            vals.append(current_reading)
            if seconds*wait_time > 20:
                # plt.plot(times[ind:], vals[ind:],color="blue")
                # plt.axis([ind, values_to_show+ ind - 1, 0, 1])
                plt.axis([times[ind], times[values_to_show+ ind - 1], 0, 100])
                ind += 1
            plt.stackplot(times, vals, color=("blue" if current_reading>treshold else "red"))
            plt.pause(0.05)

        # wait time before next reading taken
        time.sleep(wait_time)
        seconds += wait_time
        times.append(seconds)


import threading

init_settings()
t = threading.Thread(target=add_point)
t.start()
plt.show()
