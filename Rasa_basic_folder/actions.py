from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine,Price):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if Price == "lesser than 300":
		TEMP = TEMP[TEMP['Average Cost for two'].apply(lambda x: x <= 300 )]
	if Price == "more than 700":
		TEMP = TEMP[TEMP['Average Cost for two'].apply(lambda x: x > 700 )]
	if Price == "between 300 to 700":
		TEMP = TEMP[TEMP['Average Cost for two'].between(300, 700)]

	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def LocationSearch(City):
	if City in ZomatoData['City'].values:
		return 'found'
	else:
		return 'notfound'

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		response=""
		if results.shape[0] == 0:
			response= "no results"
			check_flag = 'true'
		else:
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class Check_Location(Action):
	def name(self):
		return 'action_check_location'
	
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		result = LocationSearch(City=loc)

		dispatcher.utter_message("-----"+result)
		return [SlotSet('location_found',result)]
