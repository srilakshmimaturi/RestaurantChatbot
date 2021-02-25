## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants

## another path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dfdsfaddas"}
    - slot{"location": "dfdsfaddas"}
    - action_check_location
    - slot{"location_found": "notfound"}
    - utter_say_notOperate
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants 




