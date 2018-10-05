#
# CSV Geocoder
#
# Written by Chris Casper
# Version : 1.0.6 - 2018.10.05
# License : GPL2
#
# Meant mostly for AutoTask imports. But technically can be used for any business name to street address 
# and/or latitude/longitude purposes. Uses pygeocoder, which uses Google Geocoding API.
#

import pandas
from pygeocoder import Geocoder
from pygeocoder import GeocoderError

business_geocoder = Geocoder(api_key='GOOGLE-API-HERE')

df = pandas.read_csv("ProspectList02.csv")
df['Address1'] = ' '
df['City'] = ''
df['State'] = ''
df['Country'] = ''
df['Zip'] = ''
df['CompanyType'] = 'Lead'
df['Lat'] = ''
df['Lng'] = ''

for idx, row in df.iterrows():
	try:
		address = business_geocoder.geocode(row.Company)
		df.set_value(idx, 'Address1', str("%s %s" % (address.street_number, address.route)))
		df.set_value(idx, 'City', address.city)
		df.set_value(idx, 'State',address.state)
		df.set_value(idx, 'Zip', address.postal_code)
		df.set_value(idx, 'Country', address.country)
		df.set_value(idx, 'CompanyType', "Lead")
		df.set_value(idx, 'Lat', address.latitude)
		df.set_value(idx, 'Lng', address.longitude)		
	except GeocoderError:
		continue

df.to_csv('ProspectOutput-Final.csv', encoding='utf-8', index=False)	