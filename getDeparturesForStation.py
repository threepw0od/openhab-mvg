# coding=utf-8
# Place this file into your python_mvg_api folder obtained from https://python-mvg-departures.readthedocs.io/en/latest/

import sys
import datetime
import time
date_time = datetime.datetime.now()

reload(sys)
sys.setdefaultencoding('utf-8')

from mvg_api import *

#define your preferred station here by id or name
myStation = Station("Hauptbahnhof")
departures = myStation.get_departures()

#prepare script output for openHAB
departureString="["

for departure in departures:
	departureString += "\""+(departure['product'] + ";" + departure['label'] + ";" + departure['destination'] + ";" + str(departure['departureTimeMinutes'])) + ";" + str(time.strftime('%H:%M', time.localtime(departure['departureTime'] / 1000.0))) + "\","
#remove last "," in string
departureString = departureString[:-1]
departureString += "]"
print(departureString)