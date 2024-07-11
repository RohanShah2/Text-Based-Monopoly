#Monopoly
# Mortgage Value is half of price
import random
import keyboard
import threading
import time

def esc_key_listener():
    keyboard.wait('esc')
    print("ESC key pressed. Exiting...")
    exit(0)

# Start the ESC key listener in a separate thread
esc_listener_thread = threading.Thread(target=esc_key_listener, daemon=True)
esc_listener_thread.start()
universalProperty = ""
rollNum = 0
timeInJail = 0
inJail = False
def getRent(prop):
    return propertyDict[prop][2]

def getPrice(prop):
    return propertyDict[prop][1]

def findPropPlace(place): # Put in a position get back the property
    for key in propertiesDict.keys():
        if propertiesDict[key][5] == place:
            return key
#Chance an COmmunity Helper for Monopoly
#Community and Chacne func
def communityChest(player):
    def bankError():
        print("Bank Error in Your Favor. \n Collect $200.")
        playersDict[player][1] += 200

    def streetRepairs():
        print("You Are Assessed For Street Repairs. \n $40 per House \n $115 per Hotel.")
        #Figure this out after finished with houses and hotels

    def lifeInsurance():
        print("Life Insurance Matures. \nCollect $100.")
        playersDict[player][1] += 100

    def taxRefund():
        print("Income Tax Refund. \nCollect $20.")
        playersDict[player][1] += 20
        
    def schoolTax():
        print("Pay School Tax of $150.")
        playersDict[player][1] -= 50

    def operaOpening():
        print("Grand Opera Opening. Collect $50 from every Player for opening night seats.")
        for i in range(len(playersDict) - 1):
            playersDict[player][1] += 50

    def xmasFund():
        print("XMas Fund Matures. \nCollect $100.")
        playersDict[player][1] += 100
        
    def advance():
        print("Advance to Go. \nCollect $200.")
        playersDict[player][1] += 200
        playersDict[player][0] = 0

    def goToJail():
        print("Go To Jail. Go Directly To Jail. Do Not Pass Go. Do Not Collect $200.")
        jail()

    def inheritance():
        print("You inherit $100")
        playersDict[player][1] += 100
        
    def hospitalPayment():
        print("Pay Hospital $100")
        playersDict[player][1] -= 100

    def beautySecondPlace():
        print("You Have Won Second Prize in a Beauty Contest. \nCollect $10.")
        playersDict[player][1] += 10

    def services():
        print("Recieve For Services $25")
        playersDict[player][1] += 25

    def doctorsFee():
        print("Doctors Fee. \nPay $50.")
        playersDict[player][1] -= 50

    def getOutOfJailFree():
        #Do later
        print("Not working right now")
        
    def stockSale():
        print("From sale of stock you get $45.")
        playersDict[player][1] += 45

    listOfFunc = (bankError, streetRepairs, lifeInsurance, taxRefund, schoolTax, operaOpening, xmasFund, advance, goToJail, inheritance, hospitalPayment, beautySecondPlace, services, doctorsFee, getOutOfJailFree, stockSale)

    num = random.randint(0, len(listOfFunc)-1)#Randomly pick a card
    listOfFunc[num]()#Run that card function


def chanceCards(player):

    def advanceRr():
        #do Later
        print("Not working right now")

    def advance():
        print("Advance to Go. \nCollect $200.")
        playersDict[player][1] += 200
        playersDict[player][0] = 0

    def bank():
        print("Bank Pays You Dividend Of $50.")
        playersDict[player][1] += 50

    def goBack():
        print("Go Back 3 Spaces.")
        playersDict[player][0] -= 3
        checkAvaliability(player)

    def electedChairman():
        print("You Have Beeen Elected Chairman Of The Board. Pay Each Player $50.")
        for key in playersDict:
            playersDict[player][1] -= 50
            playersDict[key][1] += 50

    def poorTax():
        print("Pay Poor Tax Of $15.")
        playersDict[player][1] -= 15

    def boardWalk():
        print("Advance Token to Boardwalk.")
        playersDict[player][0] = 39
        global universalProperty
        universalProperty = "Boardwalk"
        checkAvaliability(player)

    def loanMatures():
        print("Your Building Loan Matures. Collect $150.")
        playersDict[player][1] += 150

    def illinois():
        print("Advance to Illinois Ave.")
        playersDict[player][0] = 24
        global universalProperty
        universalProperty = "Illinois Ave."
        checkAvaliability(player)

    #There are a couple more that I need to figure out how to do later.

    listOfFunc2 = (advanceRr, advance, bank, goBack, electedChairman, poorTax, boardWalk, loanMatures, illinois)

    num = random.randint(0, len(listOfFunc2)-1)#Randomly pick a card
    listOfFunc2[num]()#Run that card function

#Property Rent
def propertyPayment(player):
    player2 = ""
    global universalProperty
    prop = universalProperty
    for key in playersDict:
        if universalProperty in playersDict[key][2] and key != player: #See who has the property and make sures its not who landed on it
                player2 = key #Assigning the owner of the property
                rentOfProp = propertiesDict[prop][2] #finding the rent of the property

                playersDict[player2][1] += rentOfProp #Adding the rent money to the owner
                playersDict[player][1] -= rentOfProp #Substracting the rent money from the player
                print("You landed on an owned property. Pay $"+ str(rentOfProp) + " in rent")

                break
        #else:
            #print("You landed on your own property")
    
def LuxuryTax(player):
    if playersDict[player][0] == 38:
        print("You landed on Luxury Tax. Pay $75")
        playersDict[player][1] -= 75
        
        
#10% or 200 for Income Tax
def IncomeTax(player):
    if playersDict[player][1] < 2000:
        playersDict[player][1] -= ((playersDict[player][1])%10)
        print("You landed on Income Tax. Pay 10% of your Money.")
            
    else:
        playersDict[player][1] -= 200
        print("You landed on Income Tax. Pay $200.")
        

#Function for railroads rent. Rail parameter is the name of the property
def railroadsPayment(player, rr):
    for key in playersDict:
        if rr in playersDict[key][2] and key != player:#See who has the rail(s) and make sures its not who landed on it
            numOfRr = 0 # Sees how many rails they have. Below too
            for i in playersDict[key][2]: #keys[2] is the property list, so checking how many they have
                if i == "Reading Railroad" or i == "Pennsylvania Railroad" or i == "B. & O. Railroad" or i == "Short Line Railroad":
                    numOfRr += 1 #Adds to numofutils if they have a utility
                        
                #Can't find an easier way to do this
            if numOfRr > 0 and numOfRr <= 4:
                payment = 25*(2**(numOfRr-1))
                print("You landed on a property which is already owned. Pay " + str(payment) + " in rent.")
                playersDict[player][1] -=  payment#Exp func because it goes 25, 50 100, etc.
                playersDict[key][1] += payment
            else:
                buying(player)
            return
        
        elif key == player and rr in playersDict[key][2]:
            print("You landed on your own railroad.")
            return

#Utility rent
def utilitiesPayment(player, utility, rollNum):
    print("Utilities Payment")
    for key in playersDict:
        if utility in playersDict[key][2] and key != player:#See who has the util(s) and make sures its not who landed on it
            numOfUtils = 0 # Sees how many utils they have. Below too
            for i in playersDict[key][2]: #keys[2] is the property list, so checking how many they have
                if i == "Electric Company" or i == "Water Works":
                    numOfUtils += 1 #Adds to numofutils if they have a utility
                        
                #Can't find an easier way to do this
            if numOfUtils == 1:
                payment = rollNum*4
                print("You landed on an owned utility. Pay "+ str(payment) + "in rent.")
                playersDict[player][1] -= rollNum*4
                playersDict[key][1] += rollNum*4
                return
            elif numOfUtils == 2:
                payment = rollNum*10
                print("You landed on an owned utility. Pay "+ str(payment) + "in rent.")
                playersDict[player][1] -= rollNum * 10 
                playersDict[key][1] += rollNum * 10
                return
            else:
                buying(player)
                return
        
        elif key == player:
            print("You landed on your own Utility.")
            return


    
    
#Buying Function
def buying(player):
    global universalProperty
    price = propertiesDict[universalProperty][1]
    buyOrNo = input("You landed on an open property. Would you like to buy "+universalProperty+" for $"+str(price)+"? ")
    if buyOrNo == "yes":
         playersDict[player][1] -= propertiesDict[universalProperty][1]
         playersDict[player][2].append(universalProperty)
         print("Great. You now own " + universalProperty)

    else:
        print("Ok")
    
    
    
#House and Hotel Func
def House(player):
    sameColor = 0
    startingColor = ""
    listOfProps = []
    for i in playersDict[player][2]:
        if sameColor == 3:
            break
        sameColor = 1
        startingColor = propertiesDict[i][0]
        for x in playersDict[player][2]:
            if x == i:
                continue
            if sameColor == 3:
                break
            if propertiesDict[x][0] == startingColor:
                sameColor += 1
                listOfProps.append(x)
            

    if sameColor == 3:
        var = int(input("You can build houses on your " + startingColor + " properties. If you would like to build houses, press 1 and explain below. If you would not, press 0."))
        if var > 0:
            print("Great. Please explain how you would like to distribute them by writing the number of houses next to each property:")
            prop1 = int(input(listOfProps[0]))#How many houses per property
            prop2 = int(input(listOfProps[1]))
            prop3 = int(input(listOfProps[2]))
            houseDict[listOfProps[0]][0] = prop1 # Updating number of houses
            houseDict[listOfProps[2]][0] = prop2
            houseDict[listOfProps[3]][3] = prop1
            playersDict[player][1] -= propertiesDict[listOfProps[0]][4] * prop1 #Subtracting money for the cost of the house
            playersDict[player][1] -= propertiesDict[listOfProps[1]][4] * prop2
            playersDict[player][1] -= propertiesDict[listOfProps[2]][4] * prop3
            #Updating rent
            propertiesDict[listOfProps[0]][2] = houseDict[listOfProps[0]][prop1+2]
            propertiesDict[listOfProps[1]][2] = houseDict[listOfProps[1]][prop2+2]
            propertiesDict[listOfProps[2]][2] = houseDict[listOfProps[2]][prop3+2]
            print("Done. All necessary actions have been taken.")
            print(propertiesDict[listOfProps[2]][2])
    else:
        print("You can't buy a house yet.")
        return
        


def parking():
    print("You are on Free Parking. Nothing happens.")

def visiting():
    print("You are just visiting jail. Nothing happens.")

def goToJail(player):
    print("You have landed on go to jail. You are now in jail and your turn is skipped.")
    inJail = True

def jail(player):
    global inJail
    global timeInJail
    if inJail and timeInJail == 3:
        print("You have spent 3 turns in jail. Now you automatically get out and your turn is skipped.")
        inJail = False
        timeInJail = 0
        return
    
    x = input("You have landed in jail. You can either pay fifty dollars to get out or see if you can roll doubles. Which do you choose, money or doubles? ")
    if x == "doubles" and inJail:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("You have chosen to roll doubles: \n"+dice1 + "\n"+dice2)
        if dice1 == dice2:
            print("Congratulations! You have rolled doubles and now advance that many spaces.")
            playersDict[player][0] += (dice1+dice2)
            timeInJail = 0
            inJail = False
            checkAvaliability(player)
            return
        if dice1 != dice2:
            print("Unfortunately, you have not rolled doubles. You will have to wait for your next turn to get out of jail.")
            timeInJail += 1
            inJail = True
            
    elif x == "money" and inJail:
        print("Great! You have chosen to pay fifty dollars to get out of jail. You are now only visitng jail and your turn is skipped.")
        playersDict[player][1] -= 50
        return
        
    

    
#Properties Dict. Color, Price, Rent, Mortgage Value, House & Hotel Cost, Place on board, Function
propertiesDict = {
    "Mediterrenean Ave." : ["Purple", 60, 2, 30, 50, 1, propertyPayment],
    "Baltic Ave." : ["Purple", 60, 4, 30, 50, 3, propertyPayment],
    "Oriental Ave." : ["Blue", 100, 6, 50, 50, 6, propertyPayment],
    "Vermont Ave." : ["Blue", 100, 6, 50, 50, 8, propertyPayment],
    "Connecticut Ave." : ["Blue", 120, 8, 60, 50, 9, propertyPayment],
    "St Charles Place" : ["Pink", 140, 10, 70, 100, 11, propertyPayment],
    "States Ave." : ["Pink", 140, 10, 70, 100, 13, propertyPayment],
    "Virginia Ave." : ["Pink", 160, 12, 80, 100, 14, propertyPayment],
    "St James Place" : ["Orange", 180, 14, 90, 100, 16, propertyPayment],
    "Tennesee Ave." : ["Orange", 180, 14, 90, 100, 18, propertyPayment],
    "New York Ave." : ["Orange", 200, 16, 100, 100, 19, propertyPayment],
    "Kentucky Ave." : ["Red", 220, 18, 110, 150, 21, propertyPayment],
    "Indiana Ave." : ["Red", 220, 18, 110, 150, 23, propertyPayment],
    "Illinois Ave." : ["Red", 240, 20, 120, 150, 24, propertyPayment],
    "Atlantic Ave." : ["Yellow", 260, 22, 130, 150, 26, propertyPayment],
    "Ventnor Ave." : ["Yellow", 260, 22, 130, 150, 27, propertyPayment],
    "Marvin Gardens" : ["Yellow", 280, 24, 140, 150, 29, propertyPayment],
    "Pacific Ave." : ["Green", 300, 26, 150, 200, 31, propertyPayment],
    "North Carolina Ave." : ["Green", 300, 26, 150, 200, 32, propertyPayment],
    "Pennsylvania Ave." : ["Green", 320, 28, 160, 200, 34, propertyPayment],
    "Park Place" : ["Dark Blue", 350, 35, 175, 200, 37, propertyPayment],
    "Boardwalk" : ["Dark Blue", 400, 50, 200, 200, 39, propertyPayment],
    
    #Utilities Blanks to match properties. Price, Mortgage Value, Place on Board, Function
    
    "Electric Company":["Blank", 150, "Blank", 75, "Blank", 12, utilitiesPayment],
    "Water Works":["Blank", 150, "Blank", 75, "Blank", 28, utilitiesPayment],
    
    #Railroads. Blanks to match properties. Price, Mortgage Value, Place on board, Function
    
    "Reading Railroad":["Blank", 200, "Blank", 100, "Blank", 5, railroadsPayment],
    "Pennsylvania Railroad":["Blank", 200, "Blank", 100, "Blank", 15, railroadsPayment],
    "B. & O. Railroad":["Blank", 200, "Blank", 100, "Blank", 25, railroadsPayment],
    "Short Line Railroad":["Blank", 200, "Blank", 100, "Blank", 35, railroadsPayment],
    

#Chance and Community Cards. WIll have Function for this. Blanks to match properties. Place on Board, Function
    
    "Community Chest 1": ["Blank", "Blank", "Blank", "Blank", "Blank", 2, communityChest],
    "Chance 1":["Blank", "Blank", "Blank", "Blank", "Blank", 7, chanceCards],
    "Community Chest 2":["Blank", "Blank", "Blank", "Blank", "Blank", 17, communityChest],
    "Chance 2":["Blank", "Blank", "Blank", "Blank", "Blank", 22, chanceCards],
    "Community Chest 3":["Blank", "Blank", "Blank", "Blank", "Blank", 33, communityChest],
    "Chance 3":["Blank", "Blank", "Blank", "Blank", "Blank", 36, chanceCards],
    
    #Miscallenous. Blanks to match properties. Place on Board, Function

    "Income Tax": ["Blank", "Blank", "Blank", "Blank", "Blank", 4, IncomeTax], # 10% or $200
    "Luxury Tax": ["Blank", "Blank", "Blank", "Blank", "Blank", 38, LuxuryTax], # - 75
    "Visiting Jail": ["Blank", "Blank", "Blank", "Blank", "Blank", 10, visiting], # Nothing Happens
    "Free Parking": ["Blank", "Blank", "Blank", "Blank", "Blank", 20, parking], #Skips Turn
    "Go to Jail": ["Blank", "Blank", "Blank", "Blank", "Blank", 30, goToJail] #Will Have Function

    }
#NUm of houses, num of hotels, regular rent, rent for 1 houese, rent for 2, 3, 4, and rent for hotel

houseDict = {
    "Mediterrenean Ave." : [0, 0, 2, 10, 30, 90, 160, 250],
    "Baltic Ave." : [0, 0, 4, 20, 60, 180, 320, 450],
    "Oriental Ave." : [0, 0, 6, 30, 90, 270, 400, 550],
    "Vermont Ave." : [0, 0, 6, 30, 90, 270, 400, 550],
    "Connecticut Ave." : [0, 0, 8, 40, 100, 300, 450, 600],
    "St Charles Place" : [0, 0, 10, 50, 150, 450, 625, 750],
    "States Ave." : [0, 0, 10, 50, 150, 450, 625, 750],
    "Virginia Ave." : [0, 0, 12, 60, 180, 500, 700, 900],
    "St James Place" : [0, 0, 14, 70, 200, 550, 750, 950],
    "Tennesee Ave." : [0, 0, 14, 70, 200, 550, 750, 950],
    "New York Ave." : [0, 0, 16, 80, 220, 600, 800, 1000],
    "Kentucky Ave." : [0, 0, 18, 90, 250, 700, 875, 1050],
    "Indiana Ave." : [0, 0, 18, 90, 250, 700, 875, 1050],
    "Illinois Ave." : [0, 0, 20, 100, 300, 750, 925, 1100],
    "Atlantic Ave." : [0, 0, 22, 110, 330, 800, 975, 1150],
    "Ventnor Ave." : [0, 0, 22, 110, 330, 800, 975, 1150],
    "Marvin Gardens" : [0, 0, 24, 120, 360, 850, 1025, 1200],
    "Pacific Ave." : [0, 0, 26, 130, 390, 900, 1100, 1275],
    "North Carolina Ave." : [0, 0, 26, 130, 390, 900, 1100, 1275],
    "Pennsylvania Ave." : [0, 0, 28, 150, 450, 1000, 1200, 1400],
    "Park Place" : [0, 0, 35, 175, 500, 1100, 1300, 1500],
    "Boardwalk" : [0, 0, 50, 200, 600, 1400, 1700, 2000]
    }

dontBuy = [
        "Income Tax", "Luxury Tax", "Visiting Jail", "Free Parking", "Go To Jail",
        "Community Chest 1", "Chance 1", "Community Chest 2", "Chance 2",
        "Community Chest 3", "Chance 3"
        ]    

closedProps = []
#Universal check if avaliable function
def checkAvaliability(player):
    global universalProperty 
    placeOnBoard = playersDict[player][0]
    
    for place in propertiesDict:
        if propertiesDict[place][5] == placeOnBoard:
            if place not in closedProps and place not in dontBuy:
                buying(player)
                closedProps.append(place)
                return
            
            if place in ["Income Tax" , "Luxury Tax" , "Community Chest 1" , "Chance 1" , "Community Chest 2" , "Chance 2" , "Community Chest 3" , "Chance 3", "Go To Jail"]:
                universalProperty = place
                propertiesDict[place][6](player)
                return
            
            if place in ["Visiting Jail" , "Free Parking"]:
                universalProperty = place
                propertiesDict[place][6]()
                return
            
            if place in ["Electric Company", "Water Works"] and place in closedProps:
                universalProperty = place
                propertiesDict[place][6](player, place, rollNum)
                return
            
            
            if place in ["Reading Railroad", "B. & O. Railroad", "Short Line Railroad", "Pennsylvania Railroad"] and place in closedProps:
                universalProperty = place
                propertiesDict[place][6](player, place)
                return
            
            #if 2 == 2:
                #print("Here's u: " + place)
            if place in houseDict.keys():
                universalProperty = place
                propertiesDict[place][6](player)
                return
            else:
                print("No worky")
                continue
    


    
    '''for u in propertiesDict:#Check where player is located on the board
        if propertiesDict[u][5] == placeOnBoard and u not in dontBuy: 
            #Update property so that the payment function can work
            universalProperty = u
            for hi in playersDict: #For each player in playersDict
                if u in playersDict[hi][2]: #If another player has the property
                    propertiesDict[u][6](player) # Run the payment function
                    return

                else:
                    buying(player) #Run the buying function
                    return
        elif (u == "Income Tax" or u == "Luxury Tax" or u == "Community Chest 1" or u == "Chance 1" or u == "Community Chest 2" or u == "Chance 2" or u == "Community Chest 3" or u == "Chance 3") and propertiesDict[u][5] == placeOnBoard:
            propertiesDict[u][6](player)
            universalProperty = u
            break'''
        
        

#Subtracts 75 for Luxury Tax

            
#Jail Func



#Getters

#Players List. Place on Board, Money, Properties, Turn Number
playersDict = {"Player 1" : [0, 1500, [], 0], "Player 2" : [0, 1500, [], 0], "Player 3" : [0, 1500, [], 0], "Player 4" : [0, 1500, [], 0]}



#Players Function
def players(playerNum):
    
    print("It is "+playerNum+"'s turn.")
    if inJail:
        jail()
        return
    if playersDict[playerNum][1] <= 0:
        print("You have run out of money and lost the game.")
        del playersDict[playerNum]
        return
    #Rolling and then updating place on board
    global rollNum
    roll = random.randint(1, 12)
    playersDict[playerNum][0] += roll
    rollNum = roll
    global universalProperty
    universalProperty = findPropPlace(playersDict[playerNum][0])
    if playersDict[playerNum][0] < 40:
        print("You rolled a "+str(roll)+". You landed on "+ str(universalProperty))
        checkAvaliability(playerNum)
        print("Place on board: "+ str(playersDict[playerNum][0]))
        print("Money: " + str(playersDict[playerNum][1]))
        print("Properties:" + str(playersDict[playerNum][2]))
        House(playerNum)
    elif playersDict[playerNum][0] > 40:
        print("You rolled a "+ str(roll) + " and pass Go. Collect $200.")
        playersDict[playerNum][1] += 200
        playersDict[playerNum][0] -= 40
        universalProperty = findPropPlace(playersDict[playerNum][0])
        checkAvaliability(playerNum)
        print("Place on board: "+ str(playersDict[playerNum][0]))
        print("Money: " + str(playersDict[playerNum][1]))
        print("Properties:" + str(playersDict[playerNum][2]))
        House(playerNum)
    elif playersDict[playerNum][0] == 0:
        print("You rolled a "+ str(roll) + " and landed on Go. Collect $200.")
    
    
    
    
i = 10

while i > 0:
    try:
        for player in playersDict:
            players(player)
            print("\n")
    except Exception:
        i += 1
        continue
    i += 1

try:
    while True:
        # Simulate some ongoing work with a sleep
        time.sleep(1)
        print("Doing some work...")
except KeyboardInterrupt:
    print("Program interrupted.")



    
        

    
    
