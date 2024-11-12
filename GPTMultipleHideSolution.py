#GOALS: 
#   Allow Players to hide and receive bonuses to their hiding based on their skill
#   Have a Monster seek them in their hiding spot


######################    MODULES USED ##############################
import random

######################    PLAYER INFORMATION ################################

#PLAYER INPUT for name and skill level
print('What is your name Traveler?')
playerName = input()
print('What is your skill level for Hiding')
pHideSkill = int(input())


######### DETERMINE MODIFIER FOR HIDING RANGE ######################
def hideModCalculation():
    
    if pHideSkill < 0:
        return 0 #RETURN SAVES VALUE FROM LOCAL TO GLOBAL SCOPE
    elif pHideSkill <=5: 
        return 1
    elif pHideSkill <=10: 
        return 2
    elif pHideSkill <= 15:
        return 3
    elif pHideSkill <=20:
        return 4
    else:
        print('You have entered a number above 20, please try again')
        return 0

pHideModifier = hideModCalculation() #RETURN VALUE PASSES AS ARGUMENT AND IS STORED
print('Your skill modifier is ' + str(pHideModifier))




###########################  DICE ROLLING ##################################

input('Press Enter to roll your D20 skill check') #HIT ENTER TO ENACT BELOW 
pHideRoll = int(random.randint(1,20)) #CHANGE NUMBER HERE TO TEST 1,20,RANDOM...
print('The number rolled is ' + str(pHideRoll))



def criticalRoll(): # WAS IT A NATURAL 20
    if pHideRoll == 20: 
        return pHideRoll
def criticalFail():# WAS IT A NATURAL 1
    if pHideRoll == 1:  
        return pHideRoll    
    
naturalTwenty = criticalRoll() # TRUE = STORES TRUE
naturalOne = criticalFail() # TRUE = STORES TRUE
########################### HIDING ROLL ####################################
def hideSkillCheck(): #PROVIDE INSIGHT TO SPACES CAN HIDE IN
    if naturalTwenty:
        print("Amazing, you rolled a " +str(pHideRoll)+ ", you gain 10 spaces to hide in")
        
    elif naturalOne:
        print("you rolled a " +str(pHideRoll)+ ", you lose 10 spaces to hide in!")
        
    else:
        print(playerName + ' will have ' + str(pHideModifier) + ' extra spaces to hide in.')
        
hideSkillCheck()#RUNS FX and STORES RESULT TO TERMINAL


def playerSpacesAndLocation(): #CREATES RANGE (HIDING SPACES) AND SPOT(LOCATION) OF YOU BASED ON RANDOM ROLL IN RANGE
                                # MONSTER PULLS THEIR GUESSING RANGE FROM THIS FUNCTION
    if naturalTwenty:
        pHidingRange = (1,31)
        #USE A TUPPLE (*) TO PULL RANGE FROM 
        pHidingSpot = random.randint (*pHidingRange) 

    elif naturalOne:
        pHidingRange = (1,11)
        pHidingSpot = random.randint(*pHidingRange)

    else:
        pHidingRange = (1,21+pHideModifier)
        pHidingSpot = random.randint(*pHidingRange)

    return pHidingSpot, pHidingRange # STORES VALUES OF EACH TO BE CALLED IN GLOBAL SCOPE

pHidingSpot, pHidingRange = playerSpacesAndLocation() #UNPACKS TUPPLE AND ASSIGNS VALUES TO GLOBAL VAR

print("Hiding Range: ", pHidingRange) 
print("Hiding Spot: ", pHidingSpot) 
print("You are now hidden.")

######################    MONSTER INFORMATION ################################

########## MONSTER TYPE and SPEED

def monsterInfo():
    monsterType = ['Demon', 'Undead', 'Elemental', 'Djinn', 'Fey', 'Beast', 'Dragon', 'Giant']
    monsterSpeed = [3,1,4,3,6]
    ###Create Dictionary to store key:value pair
    monsterStat = {}
    ###Create key value pairs from 2 lists and assign blank values 1
    for i in range(len(monsterType)):
        if i < len(monsterSpeed):
            monsterStat[monsterType[i]] = monsterSpeed[i]
        else:
            monsterStat[monsterType[i]] = 1
    return monsterStat
monsterStat = monsterInfo()
print(monsterStat)


########## WHAT MONSTER IS SEEKING YOU
input('Press Enter to see which monster is hunting you')
# var = tuple (i.e. key value pair) created since using .items
randomMonster = random.choice(list(monsterStat.items()))

#var key, var value = var name with tuple (key val pair)
monsterType, monsterSpeed = randomMonster

#monsterName = 'Slimer'
print('A '+ str(monsterType) +' has sensed your presence and is ready to find you. If you are able to stay hidden from them for 6 turns you win' + '. A '+str(monsterType) + ' can check '+ str(monsterSpeed)+ ' spaces each turn!')

input('press enter to start the hunt')

######### SET THE AREA & HOW MANY ATTEMPTS TO SEEK YOU OUT 


######### DETERMINE IF SEEKER FOUND HIDER
def playerFound(): 
    for seek in range(6): #LOOP THROUGH CODE x6
        seekRolls = random.sample(range(*pHidingRange), monsterSpeed) # RANDOM ROLL OCCURS - based on seekRange 
        print(f'{monsterType} is seeking....This is attempt number {seek + 1})')
        print(f'Monster checks places: {seekRolls}')

        if pHidingSpot in seekRolls:
            print(f'You\'ve been found in spot {pHidingSpot}. It took {seek + 1} attempts to find you.')
            print('You are mine now!!!')
            return
        remainingAttempts = 6 - (seek+1)
        print(f'Come Out Come Out Wherever You Are! {remainingAttempts} more chances remaining.')
        input("Press Enter to start the next turn")
    print(f'{monsterType} you fool! You couldn\'t find me... I win!')

playerFound() #need to call function for it to run
 







   