# Code to get weather info using Python
from my_api import *
import requests, json
from presets import *
from datetime import datetime
from presets import *
from my_lang import *
import os

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

def weather(city):
  url = base_url+city+"&appid="+api_id+"&units=metric"+"&lang="+my_lang
  response = requests.get(url)
  x = response.json()
#  print(x)
  if x["cod"] != '404' :
    os.system("clear")
    print (f"{RED}==========================================={END}")
    print (f"{VIOLET}City Name:            {CYAN}{x['name']}")
    print (f"{VIOLET}Country Name:         {CYAN}{x['sys']['country']}")
    print (f"{VIOLET}Description:          {CYAN}{x['weather'][0]['description']}")
    print (f"{VIOLET}Current Temperature:  {CYAN}{x['main']['temp']}")
    print (f"{VIOLET}Minimum Temperature:  {CYAN}{x['main']['temp_min']}")
    print (f"{VIOLET}Maximum Temperature:  {CYAN}{x['main']['temp_max']}")
    print (f"{VIOLET}Humidity:             {CYAN}{x['main']['humidity']}%")
    print (f"{VIOLET}visibility:           {CYAN}{x['visibility']/1000}km")
    print (f"{VIOLET}Wind speed:           {CYAN}{x['wind']['speed']}m/s")
    rise = x['sys']['sunrise']
    a = datetime.fromtimestamp(rise)
    print (f"{VIOLET}Sunrise:              {CYAN}{a} ")
    set = x['sys']['sunset']
    b = datetime.fromtimestamp(set) 
    print (f"{VIOLET}Sunset:               {CYAN}{b}")
    print (f"{RED}==========================================={END}")
  else :
    print (f"{RED}ERROR! No such City Found Please try again{EXIT}")
    os.system("python3 main.py")

