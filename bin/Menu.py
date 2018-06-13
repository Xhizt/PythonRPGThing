import Math
import Values


def initialize():
    print
    print
    print "    Enemy 1: ", Values.EnemyHP, "HP      ATT: ", Values.EnemyATT, "     DEF: ", Values.EnemyDEF
    print
    print
    print
    print
    print
    print
    print "    You: ", Values.PlayerHP, "HP    ", Values.PlayerMP, "MP    ATT: ", Values.PlayerATT, "   MAG: ", Values.PlayerMAG, "   DEF: ", Values.PlayerDEF
    print
    print "    Waiting for user input..."
    print
    print "    A: Attack, M: Cast Magic (Cost 25 MP), D: Defend:\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

def MenuRefresh(ExtraMessage):
    print
    print
    print "    Enemy 1: ", Values.EnemyHP, "HP      ATT: ", Values.EnemyATT, "     DEF: ", Values.EnemyDEF
    print
    print
    print
    print
    print
    print
    print "    You: ", Values.PlayerHP, "HP    ", Values.PlayerMP, "MP    ATT: ", Values.PlayerATT, "   MAG: ", Values.PlayerMAG, "   DEF: ", Values.PlayerDEF
    print
    print "    " + ExtraMessage
    print
    print "    A: Attack, M: Cast Magic (Cost 25 MP), D: Defend:\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    if Values.EnemyHP == 0:
        Math.GameOver()
    elif Values.PlayerTurn == 0:
        Math.EnemyTurn()
    else:
        Math.standby()