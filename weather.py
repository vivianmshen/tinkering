import forecastio
from geopy.geocoders import Nominatim

#api_key = "fa0f4101a8fffaf8f76ae601b8ca631a"
#lat = 37.77
#lng = -122.43

#forecast = forecastio.load_forecast(api_key, lat, lng).currently()


#for forecasts in forecast.daily().data:
#	print(forecasts.precipProbability)

def get_latitude(address):
	geolocator = Nominatim()
	return geolocator.geocode(address).latitude

def get_longitude(address):
	geolocator = Nominatim()
	return geolocator.geocode(address).longitude

def get_weather(address, api_key):
	lat = get_latitude(address)
	lng = get_longitude(address)
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()
	return "The weather is {} and {} degrees".format(forecast.summary, forecast.temperature)

address = input("What is the address you would like the weather for? ")
print(get_weather(address, "fa0f4101a8fffaf8f76ae601b8ca631a"))