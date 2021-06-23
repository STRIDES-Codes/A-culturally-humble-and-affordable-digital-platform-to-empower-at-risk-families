import requests
import os
from datetime import datetime

#user_api = os.environ["70e13cd941f66d90de87185e335ed7d7"]
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"70e13cd941f66d90de87185e335ed7d7"

api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = (((api_data['main']['temp']) - 273.15)*(9/5) +32)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = (api_data['wind']['speed']*1.609)
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
t_min = (((api_data['main']['temp_min']) - 273.15)*(9/5) +32)
t_max = (((api_data['main']['temp_max']) - 273.15)*(9/5) +32)
category = []

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg F".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :{:.2f} mph".format(wind_spd))
print ("Today's minimum temperature is  {:.2f} deg F ".format(t_min))
print ("Today's maximum temperature is  {:.2f} deg F ".format(t_max))

if temp_city > 75 and hmdt > 68:
    category = 1
elif temp_city < 75 and hmdt < 68:
    category = 2
elif temp_city > 75 and hmdt < 68:
    category = 3
elif temp_city < 75 and hmdt > 68:
    category = 4
else:
    category = 5

print("Categorization #:",category)


