
import urllib
import json

def http_web():
	request = urllib.urlopen("http://google.com")
	code = request.getcode()
	content = request.read()
	print(str(content))


def http_web_api(api):
	json_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_hour.geojson".format(api)
	request = urllib.urlopen(json_data)
	http_code = request.getcode()

	if http_code == 200:
		content = request.read()
		print(content)
	else:
		print('Sorry, we received an error : {}'.format(http_code))

http_web_api(4.5)
