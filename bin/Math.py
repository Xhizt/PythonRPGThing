import os
import pygame
import time
import Values
import Menu
import winsound
import msvcrt

# Christian Tavares | 6/14/2018 | RPGThing |
#
# This class is used for any actual calculations done in the program, as well as reading
# user input

def standby(): #Default function for awaiting user input
    while msvcrt.kbhit():
        msvcrt.getwch()   #Stops console from accepting input until everything is displayed
    UserInput = raw_input("Choose your action!('exit' to quit): ")
    TestUserInput(UserInput)

def TestUserInput(input):
    if input.lower() == "a":   #Attack
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Damage.wav").play()

        Values.EnemyHP = Values.EnemyHP - (Values.PlayerATT - Values.EnemyDEF) #Damage Formula

        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerTurn = 0
        Menu.MenuRefresh("PLAYER attacked! ENEMY took 10 damage!")  #Refresh, with message to display
    elif input.lower() == "m":  #Magic
        if Values.PlayerMP > 24:        #Test Player's MP. If not 25+, cancels action
            pygame.mixer.init()
            pygame.mixer.Sound("Sounds\Spell.wav").play()
            time.sleep(0.5)

            Values.EnemyHP = Values.EnemyHP - (Values.PlayerMAG - Values.EnemyDEF) #Damage Formula
            Values.PlayerMP = Values.PlayerMP - 25                                 #MP cost
            os.system('cls' if os.name == 'nt' else 'clear')
            Values.PlayerTurn = 0
            Menu.MenuRefresh("PLAYER casts a spell! ENEMY took 20 damage!")
        else:                                                                 #Not enough MP catch
            os.system('cls' if os.name == 'nt' else 'clear')
            Menu.MenuRefresh("Not enough MP!")
    elif input.lower() == "d":   #Defend
        time.sleep(0.5)
        Values.PlayerDefending = 1
        Values.PlayerTurn = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu.MenuRefresh("PLAYER defends!")
    elif input.lower() == "exit":#End Program
        CloseProgram();
    else:                        #Invalid
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu.MenuRefresh("Input not valid")

def EnemyTurn(): #Enemy
    time.sleep(1)
    if Values.PlayerDefending == 0:
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Damage.wav").play()

        Values.PlayerHP = Values.PlayerHP - (Values.EnemyATT - Values.PlayerDEF) #Damage Formula
        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerTurn = 1
        Menu.MenuRefresh("ENEMY attacked! PLAYER took 10 damage!")
    else: #If Player is defending
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Defense.wav").play()
        time.sleep(0.5)

        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerDefending = 0
        Values.PlayerTurn = 1
        Menu.MenuRefresh("ENEMY attacked! PLAYER blocked! 0 Damage recieved!")

def GameOver(): #Victory!
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    print
    print
    print ("\n\n\n\n\n\n\n                                  You win!\n\n\n\n\n\n\n\n\n\n\n\n")
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("Sounds\Victory.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    os.system('pause')
    quit()

def CloseProgram(): #Close Program
    quit()