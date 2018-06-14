import Math
import os
import time
import Values

# Christian Tavares | 6/14/2018 | RPGThing |
#
# This class is used simply for the menus. The initialize method only being used once at the start,
# while the MenuRefresh method is used to reload values into the console after an action is made.

def initialize():   #Displayed on opening the program
    print
    print
    print "\n\n    Enemy: ", Values.EnemyHP, "HP      ATT: ", Values.EnemyATT, "     DEF: ", Values.EnemyDEF
    print
    print
    print
    print
    print
    print
    print "    You: ", Values.PlayerHP, "HP    ", Values.PlayerMP, "MP    ATT: ", Values.PlayerATT, "   MAG: ", Values.PlayerMAG, "   DEF: ", Values.PlayerDEF
    print
    print "\n    Waiting for user input..."
    print
    print "\n\n    A: Attack, M: Cast Magic (Cost 25 MP), D: Defend:\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

def MenuRefresh(ExtraMessage):    #Used for loading variables
    print
    print
    print "\n\n    Enemy: ", Values.EnemyHP, "HP      ATT: ", Values.EnemyATT, "     DEF: ", Values.EnemyDEF
    print
    print
    print
    print
    print
    print
    print "    You: ", Values.PlayerHP, "HP    ", Values.PlayerMP, "MP    ATT: ", Values.PlayerATT, "   MAG: ", Values.PlayerMAG, "   DEF: ", Values.PlayerDEF
    print
    print "\n    " + ExtraMessage
    print
    print "\n    A: Attack, M: Cast Magic (Cost 25 MP), D: Defend:\n\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

    if Values.EnemyHP <= 0: #Victory!
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        Math.GameOver()
    elif Values.PlayerTurn == 0: #Enemy's turn
        Math.EnemyTurn()
    else:
        Math.standby() #Player's turn