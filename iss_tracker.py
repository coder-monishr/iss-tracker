
#https://www.openstreetmap.org/?mlat=25.32&mlon=-12.48#map=3/25.32/-12.48
import urllib.request 
import json
import webbrowser

api_url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(api_url)
#print(response.read())
obj = json.loads(response.read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']

url = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(long) + '#map=7/' + str(lat)+ '/' + str(long)
webbrowser.open_new(url)



