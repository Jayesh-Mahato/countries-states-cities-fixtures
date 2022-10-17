# To create data of a specific country
# This example if for Country - India (ID:101)

import json

# Countries Fixture is omitted

# ===================================================================================

# States Fixture
with open('states.json', 'r') as statefile:
	state_obj = json.load(statefile)

new_state_obj = []
state_count = 0
for state in state_obj:
	if state_obj[state_count]["country_id"]==101:
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

with open("State_Specific.json","w") as newStateFile:
	json.dump(new_state_obj, newStateFile, indent=4)

# ===================================================================================

# Cities Fixture
with open('cities.json', 'r') as cityfile:
	city_obj = json.load(cityfile)

new_city_obj = []
city_count = 0
for city in city_obj:
	if city_obj[city_count]["country_id"]==101:
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

with open("City_Specific.json","w") as newCityFile:
	json.dump(new_city_obj, newCityFile, indent=4)
