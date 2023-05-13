import os, time, random

#Classes
class player:
  def __init__(self, playername):
    self.name = str(playername)
  def getPlayerName(self):
    return str(self.name)

#Game Loop Variables    
loop_counter = 0


#Main Game Loop    
while True:
  if loop_counter == 0:
    os.system("clear")
    print("Hello and welcome to ADVENTURE!")
    name = str(input("What do we call you? -> "))
    player1 = player(str(name))
    print("You would like me to call you " + player1.getPlayerName() + ". Is this correct?")
    print("[Y/N]?")
    command = str(input("-> ")).lower()
    
    
