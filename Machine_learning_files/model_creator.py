import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import  LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pickle import load,dump

# these variables are global and is to be imported from exposed variables file
current_model,l1,l2=None,None,None

def retrain_model():
    global current_model,l1,l2
    array_data = [['001', '01-01-2021', 'clay', 1543, 'Plain', 8, 6],
                  ['002', '03-02-2021', 'sandy', 4543, 'slope', 16, 10]
                  ] * 10  # random data array loaded from the DB
    # stands for trip_id=001,date=01-01-2021,soil_type='clay',slope_type='plain',deisel=8,
    # create a new random data generator
    array_data = np.array(array_data)  # converting to np array
    data = pd.DataFrame(data=array_data, columns=['trip_id', 'date', 'stype', 'area', 'ltype', 'fuel', 'duration'])

    l1 = LabelEncoder()
    l2 = LabelEncoder()
    stype, ltype = data['stype'], data['ltype']
    data.drop(['stype', 'ltype', 'date'], axis=1, inplace=True)

    stype = l1.fit_transform(stype)
    ltype = l2.fit_transform(ltype)
    # print(ltype,'*'*10,stype)
    data['ltype'] = ltype
    data['stype'] = stype
    # data.groupby('trip_id').groups

    new_model = LinearRegression()
    X = data.drop(['duration'], axis=1)
    Y = data['duration']

    new_model.fit(X, Y)
    with open("models/current_model.pkl",'wb') as file:
        dump(new_model, file)
    with open("models/Label_encoder1.pkl",'wb') as f:
        dump(l1,f)
    with open("model/Label_encoder2.pkl",'wb') as f:
        dump(l2,f)



    print("model retrained with new data!")
    reload_current_model()


def reload_current_model():
     global current_model,l1,l2
     current_model=load(open("models/current_model.pkl","rb"))
     l1=load(open("models/Label_encoder1.pkl","rb"))
     l2 = load(open("models/Label_encoder2.pkl","rb"))
     print(current_model)
     print("load success!!")

def get_prediction(values):
    record=pd.DataFrame(np.array(values),columns=['trip_id', 'date', 'stype', 'area', 'ltype', 'fuel', 'duration'])
    stype, ltype = record['stype'], record['ltype']
    record.drop(['stype', 'ltype', 'date'], axis=1, inplace=True)
    stype = l1.fit_transform(stype)
    ltype = l2.fit_transform(ltype)
    record['ltype'] = ltype
    record['stype'] = stype
    value=current_model.predict(record)
    return value[0]

import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler


# print("start")
# def print_date_time():
#     print("helllo")


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=retrain_model, trigger="interval", seconds=3)
# scheduler.start()
#
# # atexit.register(lambda: scheduler.shutdown())
#
# # schelduler wont work if main thread is not active
# # keep the main thread active by holding the task in a flask main.py file
# print("end")

# an infinite loop to simulate flask process
# while(1):
#     pass




retrain_model()
# reload_current_model()
