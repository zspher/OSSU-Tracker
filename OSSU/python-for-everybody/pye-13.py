# $ python3 geojson.py
# Enter location: Ann Arbor, MI
# Retrieving http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42
# Retrieved 1736 characters
# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Ann Arbor",
#                     "short_name": "Ann Arbor",
#                     "types": [
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Washtenaw County",
#                     "short_name": "Washtenaw County",
#                     "types": [
#                         "administrative_area_level_2",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Michigan",
#                     "short_name": "MI",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "United States",
#                     "short_name": "US",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 }
#             ],
#             "formatted_address": "Ann Arbor, MI, USA",
#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": 42.3239728,
#                         "lng": -83.6758069
#                     },
#                     "southwest": {
#                         "lat": 42.222668,
#                         "lng": -83.799572
#                     }
#                 },
#                 "location": {
#                     "lat": 42.2808256,
#                     "lng": -83.7430378
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 42.3239728,
#                         "lng": -83.6758069
#                     },
#                     "southwest": {
#                         "lat": 42.222668,
#                         "lng": -83.799572
#                     }
#                 }
#             },
#             "place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }
# lat 42.2808256 lng -83.7430378
# Ann Arbor, MI, USA
# Enter location:
# Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
  api_key = 42
  serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
  serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  address = input('Enter location: ')
  if len(address) < 1:
    break

  parms = dict()
  parms['address'] = address
  if api_key is not False:
    parms['key'] = api_key
  url = serviceurl + urllib.parse.urlencode(parms)

  print('Retrieving', url)
  uh = urllib.request.urlopen(url, context=ctx)
  data = uh.read().decode()
  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data)
  except:
    js = None

  if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    continue

  print(json.dumps(js, indent=4))

  lat = js['results'][0]['geometry']['location']['lat']
  lng = js['results'][0]['geometry']['location']['lng']
  print('lat', lat, 'lng', lng)

  country_code = [item['short_name'] for item in js['results']
                  [0]['address_components'] if 'country' in item['types']]
  if country_code:
    print(country_code[0])
  else:
    print('No country code')

  location = js['results'][0]['formatted_address']
  print(location)
