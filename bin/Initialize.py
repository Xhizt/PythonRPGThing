import os
import winsound
import Math
import Menu

winsound.PlaySound("Sounds\Battle.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
os.system('cls' if os.name == 'nt' else 'clear')
Menu.initialize()
Math.standby()
