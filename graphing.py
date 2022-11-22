import json

with open('Study_1/sensor_data(Study_1).json', 'r') as f:
    sensor_data = json.load(f)
    print('\nSENSOR DATA')

import pandas as pd

sensor_DF = pd.DataFrame(sensor_data)
phone_DF = pd.read_csv('Study_1/phone_data(Study_1).csv')
phone_DF['phonePressure'] = phone_DF['phonePressure'].apply(lambda x: x*10)
phone_DF['speed'] = phone_DF['speed'].apply(lambda x: x*2.237)

print('\nSENSOR DATA')
print(sensor_DF)
print('\nPHONE DATA')
print(phone_DF)



full_DF = pd.concat([sensor_DF, phone_DF], axis=1)

print('\nFULL DATAFRAME')
print(full_DF)

full_DF.to_csv('allDATA.csv')