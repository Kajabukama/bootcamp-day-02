
import urllib
import json

def http_web():
	request = urllib.urlopen("http://google.com")
	code = request.getcode()
	content = request.read()
	print(content)

# a function to read json data using urllib library
# the function takes one argument which the API address
# example : http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson

def http_web_api(api):
	json_data = api
	request = urllib.urlopen(json_data)
	http_code = request.getcode()

	if http_code == 200:
		content = request.read()
		print(content)
	else:
		print('Sorry, we received an error : {}'.format(http_code))

http_web_api("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson")
