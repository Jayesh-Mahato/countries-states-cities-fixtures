import json

# Countries Fixture
# Open file for reading
with open('countries.json', 'r') as countryfile:
	# Load content from existing file
	country_obj = json.load(countryfile)

# Comment out for Understanding 
# print(country_obj[0]["name"])
# print(len(country_obj))

# Create new object for fixture
new_country_obj = []
count = 0
for country in country_obj:
	new_country_obj.append(
	{
		"model": "geodata.Country",
		"pk": count+1,
		"fields": {
			"name": country_obj[count]["name"],
			"iso3": country_obj[count]["iso3"],
			"iso2": country_obj[count]["iso2"],
			"numeric_code": country_obj[count]["numeric_code"],
			"phone_code": country_obj[count]["phone_code"],
			"capital": country_obj[count]["capital"],
			"currency": country_obj[count]["currency"],
			"currency_name": country_obj[count]["currency_name"],
			"region": country_obj[count]["region"],
			"subregion": country_obj[count]["subregion"],
			"latitude": country_obj[count]["latitude"],
			"longitude": country_obj[count]["longitude"],
		}
	}
	)
	count += 1

# Comment out for Understanding 
# print(new_country_obj[0])
# print(len(new_country_obj))
# print(new_country_obj[0]["fields"]["name"])

with open("Country.json","w") as newCountryFile:
	json.dump(new_country_obj, newCountryFile, indent=4)

# ===================================================================================

# States Fixture
with open('states.json', 'r') as statefile:
	state_obj = json.load(statefile)

new_state_obj = []
state_count = 0
for state in state_obj:
	new_state_obj.append(
	{
		"model": "geodata.State",
		"pk": state_obj[state_count]["id"],
		"fields": {
			"name": state_obj[state_count]["name"],
			"country_id": state_obj[state_count]["country_id"],
			"country_code": state_obj[state_count]["country_code"],
			"latitude": state_obj[state_count]["latitude"],
			"longitude": state_obj[state_count]["longitude"],
		}
	}
	)
	state_count += 1

with open("State.json","w") as newStateFile:
	json.dump(new_state_obj, newStateFile, indent=4)

# ===================================================================================

# Cities Fixture
with open('cities.json', 'r') as cityfile:
	city_obj = json.load(cityfile)

new_city_obj = []
city_count = 0
for city in city_obj:
	new_city_obj.append(
	{
		"model": "geodata.City",
		"pk": city_obj[city_count]["id"],
		"fields": {
			"name": city_obj[city_count]["name"],
			"state_id": city_obj[city_count]["state_id"],
			"state_code": city_obj[city_count]["state_code"],
			"country_id": city_obj[city_count]["country_id"],
			"country_code": city_obj[city_count]["country_code"],
			"latitude": city_obj[city_count]["latitude"],
			"longitude": city_obj[city_count]["longitude"],
		}
	}
	)
	city_count += 1

with open("City.json","w") as newCityFile:
	json.dump(new_city_obj, newCityFile, indent=4)
