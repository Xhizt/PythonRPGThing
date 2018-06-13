import os
import pygame
import time
import Values
import Menu

def standby():
    if (Values.EnemyHP == 0):
        GameOver()
    else:
        UserInput = raw_input()
        TestUserInput(UserInput)

def TestUserInput(input):
    if input.lower() == "a":
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Damage.wav").play()
        time.sleep(0.5)

        Values.EnemyHP = Values.EnemyHP - (Values.PlayerATT - Values.EnemyDEF)
        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerTurn = 0
        Menu.MenuRefresh("PLAYER attacked! ENEMY took 10 damage!")
    elif input.lower() == "m":
        if Values.PlayerMP > 24:
            pygame.mixer.init()
            pygame.mixer.Sound("Sounds\Spell.wav").play()
            time.sleep(0.5)

            Values.EnemyHP = Values.EnemyHP - (Values.PlayerMAG - Values.EnemyDEF)
            Values.PlayerMP = Values.PlayerMP - 25
            os.system('cls' if os.name == 'nt' else 'clear')
            Values.PlayerTurn = 0
            Menu.MenuRefresh("PLAYER casts a spell! ENEMY took 20 damage!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            Menu.MenuRefresh("Not enough MP!")
    elif input.lower() == "d":
        time.sleep(0.5)
        Values.PlayerDefending = 1
        Values.PlayerTurn = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu.MenuRefresh("PLAYER defends!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu.MenuRefresh("Input not valid")

def EnemyTurn():
    time.sleep(1)
    if Values.PlayerDefending == 0:
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Damage.wav").play()
        time.sleep(0.5)

        Values.PlayerHP = Values.PlayerHP - (Values.EnemyATT - Values.PlayerDEF)
        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerTurn = 1
        Menu.MenuRefresh("ENEMY attacked! PLAYER took 10 damage!")
    else:
        pygame.mixer.init()
        pygame.mixer.Sound("Sounds\Defense.wav").play()
        time.sleep(0.5)

        os.system('cls' if os.name == 'nt' else 'clear')
        Values.PlayerDefending = 0
        Values.PlayerTurn = 1
        Menu.MenuRefresh("ENEMY attacked! PLAYER blocked! 0 Damage recieved!")

def GameOver():
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    print
    print
    print ("    You win!")
    raw_input()