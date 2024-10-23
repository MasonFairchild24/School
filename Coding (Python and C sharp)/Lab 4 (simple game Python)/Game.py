def main():
    import time
    startGame()
    
        
#These are all just variables taht are used later in the game.
gameRunning = True #Keeps the game running
copCountDown = -1 #This and northSouthVal are the starting position
northSouthVal = 1
eastWestVal = 2
pullTheLimbDown = 0 #Just a value that when it is interacted with it becomes 1, allowing other pathways
treeStumpOver = 0  #Same as pullTheLimbDown

def startGame():
    import time #adds time before prints.
    global gameRunning
    startUp = input("""Would you like to start the game? (1-2)
1. Yes
2. No
""")
    while startUp != '1' and startUp != '2': #Just input validation
        print("Please enter the correct number")
        startUp = input("""Would you like to start the game? (1-2)
1. Yes
2. No
""")
    if startUp == '1': #Starts the game is the user inputs 1
        name = input("Please enter your name:")
        print(f"You have just escaped your prison cell and have successfully made it to the woods behind the prison.")
        time.sleep(2)
        print("Your childhood friend, Roudy Miles, has given you vague instructions on how to unlock the escape through a handwritten note that reads...")
        time.sleep(2)
        checkNote()
        print(f"You must find the escape before the cops do, hopefully you won't encounter them at all. Good luck {name}...")
        time.sleep(5)
        print("The X is where you are located.")
        map12()
        gameRun()

    elif startUp == '2':
        endGame()


def gameRun():
    global gameRunning
    while gameRunning == True:
        actionInput()
    
def endGame():
    print("Exiting the game.")
    global gameRunning
    gameRunning = False


def goNorth():
    global northSouthVal
    if(northSouthVal >= 5):
        print("There is a fence in your way, you cannot move north.")
    else:
        northSouthVal += 1
        print("You have moved north.")
        
#goSouth, goEast, goNorth, goWest are all just movements that add or subtract from the initial val, if it reaches 5 then it prevents the player from moving that way again.
def goSouth():
    global northSouthVal
    if(northSouthVal <= 1):
        print("There is a fence in your way, you cannot move south.") 
    else:
        northSouthVal -= 1
        print("You have moved south.")

def goEast():
    global eastWestVal
    if(eastWestVal >= 5):
        print("There is a fence in your way, you cannot move East.")
    else:
        eastWestVal += 1
        print("You have moved east.")

def goWest():
    global eastWestVal
    if(eastWestVal <= 1):
        print("There is a fence in your way, you cannot move West.")
    else:
        eastWestVal -= 1
        print("You have moved west.")

def actionInput(): #This entire function is just a loop with if statements that could change the loop depending on various variables. (ex. When you reach 1, 4 you can pull down the limb)
    import time
    time.sleep(1)
    copEncounter()
    if eastWestVal == 1 and northSouthVal == 4:
        if pullTheLimbDown == 0:
            print("You see a limb hanging above you, barely low enough for you to reach")
        time.sleep(2)
        actionInput = input("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. Pull down the Tree Limb
8. Exit Game
""")
        while actionInput != '1' and actionInput != '2' and actionInput != '3' and actionInput != '4' and actionInput != '5' and actionInput != '6' and actionInput != '7' and actionInput != '8':
            print("Please enter a number 1-8")
            time.sleep(2)
            actionInput = input ("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. Pull down the Tree Limb
8. Exit Game
""")
        if actionInput == '1':
            goNorth()
        elif actionInput == '2':
            goEast()
        elif actionInput == '3':
            goSouth()
        elif actionInput == '4':
            goWest()
        elif actionInput == '5':
            checkNote()
        elif actionInput == '6':
            checkMap()
        elif actionInput == '7':
            pullTreeLimb()
        elif actionInput == '8':
            endGame()



    if eastWestVal == 3 and northSouthVal == 2:
        if treeStumpOver == 0:
            print("You see a stump infront of you")
        time.sleep(2)
        actionInput = input("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. Push over the Tree Stump
8. Exit Game
""")
        while actionInput != '1' and actionInput != '2' and actionInput != '3' and actionInput != '4' and actionInput != '5' and actionInput != '6' and actionInput != '7' and actionInput != '8':
            print("Please enter a number 1-8")
            time.sleep(1)
            actionInput = input ("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. Pull over the Tree Stump
8. Exit Game
""")
        if actionInput == '1':
            goNorth()
        elif actionInput == '2':
            goEast()
        elif actionInput == '3':
            goSouth()
        elif actionInput == '4':
            goWest()
        elif actionInput == '5':
            checkNote()
        elif actionInput == '6':
            checkMap()
        elif actionInput == '7':
            pushStumpOver()
        elif actionInput == '8':
            endGame()
    
    elif (eastWestVal == 5 and northSouthVal == 4) and (pullTheLimbDown >= 1 and treeStumpOver >= 1): #This is the end of the game, checks to see if you pushed the stump over and pulled the tree limb down.
        print("You see a rock roll away from the entrance to a cave.")
        time.sleep(2)
        print("You walk into the opening before stepping onto a plate that slowly moves the rock back over the entrance, torches along the wall light the path...")
        print(f"You successfully escaped prison. Congrats")
        endGame()
    
    elif (eastWestVal == 5 and northSouthVal == 4):
        print("You see a rock covering the entrace to a cave. Next to the cave you see a Stuffed Squirrel.")
        time.sleep(2)
        actionInput = input("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. End the game
""")
        while actionInput != '1' and actionInput != '2' and actionInput != '3' and actionInput != '4' and actionInput != '5' and actionInput != '6' and actionInput != '7':
            print("Please enter a number 1-7")
            time.sleep(1)
            actionInput = input ("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. End the game
""")
        if actionInput == '1':
            goNorth()
        elif actionInput == '2':
            goEast()
        elif actionInput == '3':
            goSouth()
        elif actionInput == '4':
            goWest()
        elif actionInput == '5':
            checkNote()
        elif actionInput == '6':
            checkMap()
        elif actionInput == '7':
            endGame()

    
    
    
    

    else:
        actionInput = input("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. End the game
""")
        while actionInput != '1' and actionInput != '2' and actionInput != '3' and actionInput != '4' and actionInput != '5' and actionInput != '6' and actionInput != '7':
            print("Please enter a number 1-7")
            time.sleep(1)
            actionInput = input ("""Would you like to:
1. Go North
2. Go East
3. Go South
4. Go West
5. Check Note
6. Check position/Map
7. End the game
""")
        if actionInput == '1':
            goNorth()
        elif actionInput == '2':
            goEast()
        elif actionInput == '3':
            goSouth()
        elif actionInput == '4':
            goWest()
        elif actionInput == '5':
            checkNote()
        elif actionInput == '6':
            checkMap()
        elif actionInput == '7':
            endGame()




def copEncounter(): #This is just a random encounter that uses a randomint to decide if you encounter a cop. (1/12 chance)
    import random
    import time
    copNum = random.randint(1, 12)
    if copNum == 7:
        copNumAnswer = input(""" You see a cop searching for you and the exit. Would you like to:
1. Hide
2. Fight
""")#Lets the player decide if they want to fight or hide
        while copNumAnswer != '1' and copNumAnswer != '2': #input Validation
            print("Please enter a valid number. (1-2)")
            time.sleep(1)
            copNumAnswer = input(""" You see a cop searching for you and the exit. Would you like to:
1. Hide
2. Fight
""")
        if copNumAnswer == '1': #if the player hides, it starts hideNotFight which is a counter. 
            hideNotFight()
            time.sleep(1)
            
        elif copNumAnswer == '2': #If the player fights, its a 1/5 chance to immediately end the game. If they win the fight it doesn't initiate the count down
            fightNotHide()


def hideNotFight(): #This gives the player 29 more turns to find the exit (very generous)
    global copCountDown
    copCountDown = 29
    print("Since you decided the hide, the cop is still searching for the exit. You better hurry.")

def fightNotHide():
    import random
    import time
    fightOrHide = input("""Are you sure you want to fight the cop instead of hiding?
1. Yes
2. No, I would rather hide
""")
    while fightOrHide != '1' and fightOrHide != '2':
        print("Please enter a valid number. (1-2)")
        time.sleep(1)
        fightOrHide = input("""Are you sure you want to fight the cop instead of hiding?
1. Yes
2. No, I would rather hide
""")
    if fightOrHide == '1':
        copChance = random.randint(1, 5)
        if copChance == 4:
            print("You tried to fight the cop and lost. You have been sent back to your cell. Game Over")
            endGame()
        else:
            print("You successfully overpowered the cop and subdued him.") #lets the player continue without the worry about the cop countdown ticking.





    



def pullTreeLimb():
    import time
    global pullTheLimbDown
    if pullTheLimbDown == 0:
        pullTheLimbDown += 1
        print("You pulled down the tree limb and heard a click.") #This whole function just adds 1 to the pullTheLimbDown function for later use, then doesnt let the value get above 1
        time.sleep(2)
    else:
        print("You already pulled the limb down.")
        time.sleep(2)
        

def pushStumpOver():
    global treeStumpOver
    if treeStumpOver == 0:
        treeStumpOver += 1
        print("You pushed the tree stump over and heard a mechanical noise underneath it") #Same thing as the pullTreeLimb function
    else:
        print("You already pushed the stump over")



def checkNote(): #This entire function just prints the note that was displayeda t the beginning so the player can read through it for the clues again.
    import time
    print("""

    "Hopefully you found this in your pocket before you do anything too stupid.
""")
    time.sleep(2)
    print("""   Remember the days we climbed that one tree as kids and used to pull on the Low Hanging Limb to pull ourselves up?
""")
    print("""   The same tree that we climbed into and threw snowballs at the park workers trying to decorate it for christmas.""")
    time.sleep(2)
    print("""
    Or the days where we would hunt with your dad behind your house, using the Broken Stump you Pushed Over as a rest for the rifle.""")
    print("""
    I still remember the day you thought you nailed that deer only to hit a squirrel next to it.
""")
    time.sleep(2)
    print("""   Can't wait til we can live like that again once we get out."
""")
    


def checkMap(): #This just checks the north/south and east/west and pritns tthe appropraite map
    if northSouthVal == 1 and eastWestVal == 1:
        map11()
    elif northSouthVal == 1 and eastWestVal == 2:
        map12()
    elif northSouthVal == 1 and eastWestVal == 3:
        map13()
    elif northSouthVal == 1 and eastWestVal == 4:
        map14()
    elif northSouthVal == 1 and eastWestVal == 5:
        map15()
    elif northSouthVal == 2 and eastWestVal == 1:
        map21()
    elif northSouthVal == 2 and eastWestVal == 2:
        map22()
    elif northSouthVal == 2 and eastWestVal == 3:
        map23()
    elif northSouthVal == 2 and eastWestVal == 4:
        map24()
    elif northSouthVal == 2 and eastWestVal == 5:
        map25()
    elif northSouthVal == 3 and eastWestVal == 1:
        map31()
    elif northSouthVal == 3 and eastWestVal == 2:
        map32()
    elif northSouthVal == 3 and eastWestVal == 3:
        map33()
    elif northSouthVal == 3 and eastWestVal == 4:
        map34()
    elif northSouthVal == 3 and eastWestVal == 5:
        map35()
    elif northSouthVal == 4 and eastWestVal == 1:
        map41()
    elif northSouthVal == 4 and eastWestVal == 2:
        map42()
    elif northSouthVal == 4 and eastWestVal == 3:
        map43()
    elif northSouthVal == 4 and eastWestVal == 4:
        map44()
    elif northSouthVal == 4 and eastWestVal == 5:
        map45()
    elif northSouthVal == 5 and eastWestVal == 1:
        map51()
    elif northSouthVal == 5 and eastWestVal == 2:
        map52()
    elif northSouthVal == 5 and eastWestVal == 3:
        map53()
    elif northSouthVal == 5 and eastWestVal == 4:
        map54()
    elif northSouthVal == 5 and eastWestVal == 5:
        map55()



#Maps, they just take up alot of room and display where the user is.

def map11():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    | X |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map12():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   | X |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map13():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   | X |   |   |
    +---+---+---+---+---+
              S
    """)

def map14():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   | X |   |
    +---+---+---+---+---+
              S
    """)
def map15():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   | X |
    +---+---+---+---+---+
              S
    """)
def map21():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    | X |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map22():
   print("""  
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   | X |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map23():
    print(""" 
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   | X |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map24():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   | X |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map25():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   | X |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map31():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W | X |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map32():
   print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   | X |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map33():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   | X |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map34():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   | X |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map35():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   | X | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map41():
   print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    | X |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map42():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   | X |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map43():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   | X |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map44():
   print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   | X |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map45():
   print("""
              N
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   | X |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map51():
    print("""
              N
    +---+---+---+---+---+
    | X |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map52():
    print("""
              N
    +---+---+---+---+---+
    |   | X |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map53():
    print("""
              N
    +---+---+---+---+---+
    |   |   | X |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)

def map54():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   | X |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
def map55():
    print("""
              N
    +---+---+---+---+---+
    |   |   |   |   | X |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
  W |   |   |   |   |   | E
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
    |   |   |   |   |   |
    +---+---+---+---+---+
              S
    """)
main()