import os
import winsound
import Math
import Menu

# Christian Tavares | 6/14/2018 | RPGThing |
#
# This class is used like a Main class. It all begins here.

winsound.PlaySound("Sounds\Battle.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
os.system('cls' if os.name == 'nt' else 'clear')
Menu.initialize() #Create Menu
Math.standby()    #Await user input