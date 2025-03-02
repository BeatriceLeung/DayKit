import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry


# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


def getTemperature():
	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 34.0522,
		"longitude": -118.2437, # UCLA
		"current": "temperature_2m",
		"daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
		"temperature_unit": "fahrenheit",
		"timezone": "America/Los_Angeles",
		"forecast_days": 1
	}
	responses = openmeteo.weather_api(url, params=params)

	response = responses[0]

	# Current values. The order of variables needs to be the same as requested.
	current = response.Current()

	current_temperature_2m = current.Variables(0).Value()

	print(f"Current temperature_2m {current_temperature_2m}")
	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
	daily_precipitation_probability_max = daily.Variables(2).ValuesAsNumpy()

	print("Daily max(F): ", daily_temperature_2m_max)
	print("Daily min(F): ", daily_temperature_2m_min)
	print("Precipitation probability(%): ", daily_precipitation_probability_max)

	return {"current": current_temperature_2m, "min": daily_temperature_2m_min[0],
		"max" : daily_temperature_2m_max[0], "preciptation_prob": daily_precipitation_probability_max[0]}
