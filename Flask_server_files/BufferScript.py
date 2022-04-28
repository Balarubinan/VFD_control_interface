import time
from random import random
startTime,endTime=-1,-1
movTime,lastTime=0,-1
def tractorStarted():
    global startTime
    startTime=time.time()
    actTime=0
    print("Started @",startTime)

def tractorStoped():
    global endTime
    endTime=time.time()
    print("Ended @",endTime)

def getActTime():
    global startTime,endTime
    res=endTime-startTime
    startTime,endTime=-1,-1
    return res

def getClientId():
    # implement name to id search
    return "RecklessRubin"

def simultateRotaryEncoder():
    # 80% time on
    # move this to RPI operations in Raspi!
    global movTime,lastTime
    # print("Calling")
    moving=random()>0.2
    # moving=pi.read(someGPOIO) or something
    if not moving:
        curTime=time.time()
        print("added"+str(curTime-lastTime))
        # random values are added but why?? fix this
        movTime+=(curTime-lastTime)
        lastTime=-1
    else:
        if lastTime==-1:
            lastTime=time.time()
    return random()>0.2

def getMovTime():
    global movTime
    return movTime

#tractorStarted()
# time.sleep(5)
# tractorStoped()
# print(getTime())
# works fine!!