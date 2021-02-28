## location_cuisine_valid_with_email
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
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details


## location_invalid_retry_with_email
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
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details

## default_location_specified_cuisine_valid_with_email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail	
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details


## location_cuisine_specified_valid_with_email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_check_location    
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail	
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details

## location_invalid_retry_deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Invalid"}
    - action_check_location
    - slot{"location_found": "notfound"}
    - utter_say_notOperate
    - utter_ask_location_retry	
* deny
    - utter_deny
    - utter_goodbye
    - action_slot_reset
    - action_restart



## location_cuisine_valid_email_deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail	
* deny
    - utter_deny
    - utter_goodbye
    - action_slot_reset
    - action_restart

## no_greet_location_cuisine_valid_with_email
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
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details


## no_greet_location_invalid_retry_with_email
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
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "aiana.goyal@upgrad.com"}
    - slot{"email": "aiana.goyal@upgrad.com"}
    - email_restaurant_details



