# Code to save the user inputted API into a file and use it as a module .
from presets import *
import time
import os

os.system("clear")
print (f"{GREEN}TO generate API, create account at \'{CYAN}https://openweathermap.org/\'")
print (f"{GREEN}Then you can get you API at \'{CYAN}https://home.openweathermap.org/api_keys\'")
print (f"{VIOLET}You don't need to save you API every time.")
time.sleep(3)
print ()
print (f"{RED}======================================================")
inp = input(f"{VIOLET}Pease Enter your api:{YELLOW} ")
print (f"{RED}======================================================")
print()
if True :
  x = open('my_api.py', 'w')
  out = "# Your API key is saved here \napi_id = \""+inp+"\""
  x.write(out)
  print(f"{HIGHLIGHT}{RED}API key saved sucessfully.{END}")
else :
  print(f"{HIGHLIGHT}{RED}ERROR please check you resources")
time.sleep(3)
