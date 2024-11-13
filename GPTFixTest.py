import random

######################    PLAYER INFORMATION ################################

# Validate Player Name Input
def validatePName():
    while True:
        playerName = input('What is your name, Traveler? ')
        if playerName.strip():  # strip removes white space at begin or end of text
            return playerName
        else:
            print("Invalid input. Please enter a valid name.")

playerName = validatePName()

# Validate Player Skill Level Input
def validatePSkill():
    while True:
        print('What is your skill level for Hiding (0-20)?')
        try:
            pHideSkill = int(input())
            if 0 <= pHideSkill <= 20:
                return pHideSkill
            else:
                print('Please enter a number between 0 and 20.')
        except ValueError:
            print('Invalid input. Please enter an integer between 0 and 20.')

pHideSkill = validatePSkill()

######### DETERMINE MODIFIER FOR NUMBER OF SPACES FOR HIDING ######################
def hideModCalculation(skill):
    if skill <= 0:
        return 0
    elif skill <= 5:
        return 1
    elif skill <= 10:
        return 2
    elif skill <= 15:
        return 3
    elif skill <= 20:
        return 4

pHideModifier = hideModCalculation(pHideSkill)  # Return value passes as argument and is stored
print('Your skill modifier is ' + str(pHideModifier))

###########################  DICE ROLLING ##################################

input('Press Enter to roll your D20 skill check')  # Hit Enter to enact below 
pHideRoll = int(random.randint(1, 20))  # Roll a D20 dice
print('The number rolled is ' + str(pHideRoll))

def criticalRoll():
    if pHideRoll == 20:
        return pHideRoll

def criticalFail():
    if pHideRoll == 1:
        return pHideRoll

naturalTwenty = criticalRoll()
naturalOne = criticalFail()

########################### HIDING ROLL ####################################
def hideSkillCheck():
    if naturalTwenty:
        print("Amazing, you rolled a " + str(pHideRoll) + ", you gain 10 spaces to hide in.")
    elif naturalOne:
        print("Oh no, you rolled a " + str(pHideRoll) + ", you lose 10 spaces to hide in!")
    else:
        print(playerName + ' will have ' + str(pHideModifier) + ' extra spaces to hide in.')

hideSkillCheck()

def playerSpacesAndLocation():
    if naturalTwenty:
        pHidingRange = (1, 31)
    elif naturalOne:
        pHidingRange = (1, 11)
    else:
        pHidingRange = (1, 21 + pHideModifier)

    print(f"You can choose a hiding spot within the range of {pHidingRange[0]} and {pHidingRange[1] - 1}.")

    while True:
        try:
            pHidingSpot = int(input(f"Enter your hiding spot (between {pHidingRange[0]} and {pHidingRange[1] - 1}): "))
            if pHidingSpot in range(*pHidingRange):
                return pHidingSpot, pHidingRange
            else:
                print(f"Invalid spot. Please choose a number between {pHidingRange[0]} and {pHidingRange[1] - 1}.")
        except ValueError:
            print(f"Invalid input. Please enter an integer between {pHidingRange[0]} and {pHidingRange[1] - 1}.")

pHidingSpot, pHidingRange = playerSpacesAndLocation()
print("Hiding Range: ", pHidingRange)
print("Hiding Spot: ", pHidingSpot)
print("You are now hidden.")

######################    MONSTER INFORMATION ################################

def monsterInfo():
    monsterType = ['Demon', 'Undead', 'Elemental', 'Djinn', 'Fey', 'Beast', 'Dragon', 'Giant']
    monsterSpeed = [3, 1, 4, 3, 6]
    monsterStat = {}
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
randomMonster = random.choice(list(monsterStat.items()))
monsterType, monsterSpeed = randomMonster

print('A ' + str(monsterType) + ' has sensed your presence and is ready to find you. If you are able to stay hidden from them for 6 turns you win. A ' + str(monsterType) + ' can check ' + str(monsterSpeed) + ' spaces each turn!')

input('Press Enter to start the hunt')

######### DETERMINE IF SEEKER FOUND HIDER
def playerFound():
    for seek in range(6):
        seekRolls = random.sample(range(*pHidingRange), monsterSpeed)
        print(f'{monsterType} is seeking... This is attempt number {seek + 1}')
        print(f'Monster checks places: {seekRolls}')

        if pHidingSpot in seekRolls:
            print(f'You\'ve been found in spot {pHidingSpot}. It took {seek + 1} attempts to find you.')
            print('You are mine now!!!')
            return
        remainingAttempts = 6 - (seek + 1)
        print(f'Come Out Come Out Wherever You Are! {remainingAttempts} more chances remaining.')
        input("Press Enter to start the next turn")
    print(f'{monsterType} you fool! You couldn\'t find me... I win!')

playerFound()
