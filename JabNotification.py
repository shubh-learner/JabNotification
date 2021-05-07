# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:05:07 2021

@author: Shubh Arya
"""

import requests
import time
import datetime


while True:
    date = datetime.datetime.now()
    dateToday = date.strftime("%d-%m-%Y")
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=363&date={}'.format(dateToday)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"})
    try:
        Dict = response.json()
        msg = ""

        for x in range(len(Dict['centers'])):
            if (Dict['centers'][x]['sessions'][0]['min_age_limit'] == 45 and Dict['centers'][x]['sessions'][0]['available_capacity'] >= 40 ):
                locmsg = ( "\nPIN Code:       " +  str(Dict['centers'][x]['pincode']) + "\n" +
                          "Address:        " + Dict['centers'][x]['address'] + "\n" +
                          "Vaccine Name:   " + Dict['centers'][x]['sessions'][0]['vaccine'] + "\n" +
                          "Age Limit:      " + str(Dict['centers'][x]['sessions'][0]['min_age_limit']) + "\n" +
                          "Number of Slots:" + str(Dict['centers'][x]['sessions'][0]['available_capacity']) + "\n" +
                          "DATE available: " + str(Dict['centers'][x]['sessions'][0]['date'])+ "\n" +
                          
                          "*****************************************" )
                msg+= locmsg

        baseURL = 'https://api.telegram.org/bot1859416700:AAFmOu1hoHLqcHmCenLMzlKUfLU6GBQkCjo/sendMessage?chat_id=-577156311&text={}'.format(msg)
        requests.get(baseURL)
        time.sleep(20)
    
    except ValueError:
        print("Response content is not valid JSON")
        time.sleep(2000)
     
 


        
        


