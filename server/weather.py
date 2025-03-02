from openmeteopy import OpenMeteo
from openmeteopy.options import EcmwfOptions
from openmeteopy.hourly import HourlyEcmwf
from openmeteopy.utils.constants import *

# Latitude, Longitude
longitude = 34.07
latitude =  -118

hourly = HourlyEcmwf()
# Here we want to see the data of past days too,notice how the timezone parameter is non existent for these api options
options =  EcmwfOptions(latitude,
                        longitude,
                        past_days=2)

mgr = OpenMeteo(options, hourly.all())

# Download data in json format
meteo = mgr.get_json_str()

print(meteo)