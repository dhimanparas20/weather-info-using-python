import module
import os
import time
from presets import *
from code import *
from my_api import *

os.system("clear")
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print (RED+"#------------------==================================================---------------------#")
print ("#------------------"+HIGHLIGHT+GREEN+"| WELCOME TO COMPILING SCRIPTS BY MST PRODUCTIONS|"+END+RED+"---------------------#")
print ("#------------------==================================================---------------------#")
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#----------------------------------------------------------------------"+HIGHLIGHT+CYAN+"BY: Paras Dhiman --#"+END)
print ()
time.sleep(2)

print (RED+"------------------------------------------------")
print (VIOLET+"            Choose your Choice                  ")
print (RED+"------------------------------------------------")
print (GREEN+"0: Save my api key")
print ("1: Get weather information")
print ("2: Change default language(beta)")
print ("69: Exit"+END)
print (RED+"================================================")
inp = int(input(CYAN+"Enter your choice :"))
print (RED+"================================================")
print()

if inp == 0:
  os.system("python3 gen_api.py")
  os.system("python3 main.py")

elif inp == 1:
  city = input("Enter the name of city: ")
  print (RED+"------------------------------------------------"+END)
  module.weather(city)
  choice = input(f"{YELLOW}Do you want to return to main menue or not?|type y or n:")
  if choice == 'Y' or choice == 'y':
      os.system("python3 main.py")
  elif choice == 'n' or choice  == 'N':
      exit()
  else:
     print(f"{VIOLET}WRONG INPUT! EXITING")
     exit()

elif inp == 2:
  os.system("clear")
  print("visit here 'https'to see the available language codes. Note language change will only appear in the output section")
  print (f"{RED}======================================================")
  lang = input(f"{CYAN}Enter the language code: ")
  print (f"{RED}======================================================")
  x = open('my_lang.py', 'w')
  out = "#Your default language is saved here \nmy_lang = \""+lang+"\""
  x.write(out)
  print(f"{HIGHLIGHT}{RED}Default language is set  to {lang}{END}")

elif inp == 69:
  print(f"{HIGHLIGHT}{RED} EXITING{END}")
  time.sleep(3)
  exit()
else :
  print(f"{RED} ERROR! Wrong input, Please try again{END}")
  time.sleep(2)
  os.system("python3 main.py")

  
