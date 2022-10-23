#!/bin/bash

#user enters a zipcode  
read -p "Please enter a zipcode" zip

#curl command used to make GET request method to request data/info about that zipcode from the API
URL=$(curl --location --max-time 30 --request GET "http://api.zippopotam.us/us/${zip}") 

#sets variable to only get the HTTP response code
curl_status=$(curl -s "http://api.zippopotam.us/us/${zip}" -o /dev/null -w '%{response_code}')

 #if the response code from http page is not "200" then echo the statement & status, otherwise, output the information from URL to JSON file
if [[ $curl_status != 200 ]]; then
 echo "Response status not OK; $curl_status"
 exit 1
else
 echo $URL > test.json
 exit 0 
  
fi
