import usb
dev=usb.core.find(idVendor=0x0403, idProduct=0x6014)
print(dev)
import board
import digitalio
print(dir(board))
import adafruit_bme680

cs = digitalio.DigitalInOut(board.D4)
spi = board.SPI()

bme680 = adafruit_bme680.Adafruit_BME680_SPI(spi, cs)
bme680.sea_level_pressure = 1013.25

sensorData = {
    'time' : [],
    'temperature':[],
    'gas' : [],
    'relative_humidity' : [],
    'pressure' : [],
    'altitude' : []
            }

import datetime as dt
import time

startTime = dt.datetime.now()
endTime = startTime + dt.timedelta(minutes=25)
nowTime = startTime

while nowTime < endTime:
    dataTypes = {
    'time' : dt.datetime.now().isoformat(),
    'temperature' : bme680.temperature,
    'gas' : bme680.gas,
    'relative_humidity' : bme680.relative_humidity,
    'pressure' : bme680.pressure,
    'altitude' : bme680.altitude
    }

    for key in dataTypes:
        sensorData[key].append(dataTypes[key])
    print(dataTypes)
    time.sleep(1/3)
    nowTime = dt.datetime.now()

import json

with open('sensor_data.json', 'w') as fp:
    json.dump(sensorData, fp, indent=4)