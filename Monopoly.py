from random import choice
import time
from HumanTime import TimeAutoShort as ta
from commaNumber import commaNumber as cn

CHECK_EVERY = 100000 # This variable limits how often to check if it's time to update the percentage and times. If it takes longer than 'freq' seconds for the percentage to be printed consider reducing this value. It checks every CHECK_EVERY dice throws. 
DIGITS = 2 # Number of digits after the decimal place
CHANCE = [0, 24, 11, 12 or 28, 5 or 15 or 25 or 35, None, 'gof', 'mvbkwds', 'gtj', None, None, 5, 39, None, None, None] # Represents spaces the player must move to according to cards in the chance deck. None represents cards which don't make the player move, gof is a get out free card, mvbkwds means move backwards and gtj means go to jail
CHEST = [0, None, None, None, 'gof', 'gtj', None, None, None, None, None, None, None, None, None, None, None] # Represents speces the player must move to according to cards in the community chest deck 

def chance():
    'Picks a card from chance deck'
    return choice(CHANCE)
def chest():
    'Picks a card from community chest deck'
    return choice(CHEST)

def generateProperties():
    'Creates a dictionary associating property names in order with ascending integers'
    properties = ['Go', 'Mediterranean Ave', 'Community Chest', 'Baltic Ave', 'Income Tax', 'Reading Railroad', 'Oriental Ave', 'Chance', 'Vermont Ave', 'Connecticut Ave', 'Jail', 'St. Charles Pl', 'Electric Co', 'States Ave', 'Virginia Ave', 'Pennsylvania Railroad', 'St. James Pl', 'Community Chest', 'Tennessee Ave', 'New York Ave', 'Free Parking', 'Kentucky Ave', 'Chance', 'Indiana Ave', 'Illinois Ave', 'B&O Railroad', 'Atlantic Ave', 'Ventnor Ave', 'Water Works', 'Marvin Gardens', 'Go to Jail', 'Pacific Ave', 'North Carolina Ave', 'Community Chest', 'Pennsylvania Ave', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']
    return dict(zip(range(len(properties)), properties))

def rollDice():
    'Returns two random numbers between 1 and 6 inclusive'
    sides = (1, 2, 3, 4, 5, 6)
    return choice(sides), choice(sides)

def monopoly(dice_throws, freq):
    'Simulates a game piece moving for dice_throw many dice throws and updates the progress every freq seconds. Statistics are printed to stdout.'
    properties = generateProperties()
    propertiesFreq = {}
    injail = False
    GetOutFree = 0
    for i in properties.values():
        propertiesFreq[i] = 0
    spaces_moved = 0
    roundsinjail = 0
    doubles_in_a_row = 0
    lastTime = itime = time.time()
    for i in range(dice_throws):
        """This block rolls the dice injail is False and updates spaces_moved"""
        if injail == False:
            a, b = rollDice()
            spaces_moved += a+b
            if a == b:
                doubles_in_a_row += 1
            else:
                doubles_in_a_row = 0
        else:
            pass
        if doubles_in_a_row >= 3:
            injail = True
            doubles_in_a_row = 0
        propertiesFreq[properties[spaces_moved%40]] += 1
        """This block decides the how prisoners are treated based on identical dice throws, get out of jail cards, and number of dice throws"""
        if spaces_moved%40 == 30:
            spaces_moved = 10
            injail = True
        if injail == True:
            a, b = rollDice()
            if a == b:
                injail = False
                roundsinjail = 0
            elif GetOutFree>0:
                injail = False
                roundsinjail = 0
                GetOutFree -= 1
            else:
                roundsinjail += 1
            if roundsinjail >= 3:
                roundsinjail = 0
                injail = False
        """This block handles the distribution and processing of chance cards and what they mean"""
        if properties[spaces_moved%40] == 'Chance':
            C = chance()
            if C == None:
                pass
            elif C == 'gof':
                GetOutFree += 1
            elif C == 'mvbkwds':
                spaces_moved -= 3
                propertiesFreq[properties[spaces_moved%40]] += 1
            elif C == 'gtj':
                injail = True
                spaces_moved = 10
                propertiesFreq[properties[spaces_moved%40]] += 1
            else:
                spaces_moved = C
                propertiesFreq[properties[spaces_moved%40]] += 1
        """This block handles the distribution and processing of chance cards and what they mean"""
        if properties[spaces_moved%40] == 'Community Chest':
            C = chest()
            if C == None:
                pass
            elif C == 'gof':
                GetOutFree += 1
            elif C == 'gtj':
                injail = True
                spaces_moved = 10
                propertiesFreq[properties[spaces_moved%40]] += 1
            else:
                spaces_moved = C
                propertiesFreq[properties[spaces_moved%40]] += 1
        if i%CHECK_EVERY == 0 and time.time() > lastTime + freq:
            percentage = float(i)/((dice_throws)/100)
            lastTime = time.time()
            timeElapsed = time.time()-itime
            humanReadableTime = ta(timeElapsed, DIGITS)
            totalEstimatedTime = (dice_throws/float(i)) * timeElapsed
            remainingReadableTime = ta(totalEstimatedTime - timeElapsed, DIGITS)
            print(f'{percentage}% complete and {humanReadableTime} elapsed')
            print(f'At this rate, {remainingReadableTime} remaining')
    print(f'100% complete {ta(time.time()-itime, DIGITS)} elapsed')
    propertiesFreqRVS = {j:i for i, j in propertiesFreq.items()}
    moveslist = []
    proplist = []
    while len(propertiesFreqRVS)>0:
        maxmoves = 0
        for i in propertiesFreqRVS:
            if i>maxmoves:
                maxmoves = i
        moveslist.append(maxmoves)
        proplist.append(propertiesFreqRVS[maxmoves])
        propertiesFreqRVS.pop(maxmoves)
    ct = 0
    print(f'The dice were rolled a total of {cn(dice_throws)} times')
    for i in moveslist:
        print(f'{proplist[ct]} was landed on {cn(i)} times and was visited {100*i/float(dice_throws)}% of dice rolls')
        ct += 1


def monopolyw(dice_throws, freq, outfile):
    'Simulates a game piece moving for dice_throw many dice throws and updates the progress every freq seconds. Statistics are saved in outfile.'
    out = open(outfile, 'w')
    properties = generateProperties()
    propertiesFreq = {}
    doubles_in_a_row = 0
    injail = False
    GetOutFree = 0
    for i in properties.values():
        propertiesFreq[i] = 0
    spaces_moved = 0
    roundsinjail = 0
    itime = time.time()
    lastTime = itime = time.time()
    for i in range(dice_throws):
        """This block rolls the dice injail is False and updates spaces_moved"""
        if injail == False:
            a, b = rollDice()
            spaces_moved += a + b
            if a == b:
                doubles_in_a_row += 1
            else:
                doubles_in_a_row = 0
        else:
            pass
        if doubles_in_a_row >= 3:
            injail = True
            doubles_in_a_row = 0
        propertiesFreq[properties[spaces_moved%40]] += 1
        """This block decides the how prisoners are treated based on identical dice throws, get out of jail cards, and number of dice throws"""
        if spaces_moved%40 == 30:
            spaces_moved = 10
            injail = True
        if injail == True:
            a, b = rollDice()
            if a == b:
                injail = False
                roundsinjail = 0
            elif GetOutFree>0:
                injail = False
                roundsinjail = 0
                GetOutFree -= 1
            else:
                roundsinjail += 1
            if roundsinjail >= 3:
                roundsinjail = 0
                injail = False
            #print('roundsinjail=={}'.format(roundsinjail))
        """This block handles the distribution and processing of chance cards and what they mean"""
        if properties[spaces_moved%40] == 'Chance':
            C = chance()
            if C == None:
                pass
            elif C == 'gof':
                GetOutFree += 1
            elif C == 'mvbkwds':
                spaces_moved -= 3
                propertiesFreq[properties[spaces_moved%40]] += 1
            elif C == 'gtj':
                injail = True
                spaces_moved = 10
                propertiesFreq[properties[spaces_moved%40]] += 1
            else:
                spaces_moved = C
                propertiesFreq[properties[spaces_moved%40]] += 1
        """This block handles the distribution and processing of chance cards and what they mean"""
        if properties[spaces_moved%40] == 'Community Chest':
            C = chest()
            if C == None:
                pass
            elif C == 'gof':
                GetOutFree += 1
            elif C == 'gtj':
                injail = True
                spaces_moved = 10
                propertiesFreq[properties[spaces_moved%40]] += 1
            else:
                spaces_moved = C
                propertiesFreq[properties[spaces_moved%40]] += 1
        if i%CHECK_EVERY == 0 and time.time() > lastTime + freq:
            percentage = float(i)/((dice_throws)/100)
            lastTime = time.time()
            timeElapsed = time.time()-itime
            humanReadableTime = ta(timeElapsed, DIGITS)
            totalEstimatedTime = (dice_throws/float(i)) * timeElapsed
            remainingReadableTime = ta(totalEstimatedTime - timeElapsed, DIGITS)
            print(f'{percentage}% complete and {humanReadableTime} elapsed')
            print(f'At this rate, {remainingReadableTime} remaining')
    print(f'100% complete {ta(time.time()-itime, DIGITS)} elapsed')
    propertiesFreqRVS = {j:i for i, j in propertiesFreq.items()}
    moveslist = []
    proplist = []
    while len(propertiesFreqRVS)>0:
        maxmoves = 0
        for i in propertiesFreqRVS:
            if i>maxmoves:
                maxmoves = i
        moveslist.append(maxmoves)
        proplist.append(propertiesFreqRVS[maxmoves])
        propertiesFreqRVS.pop(maxmoves)
    ct = 0
    out.write(f'The dice were rolled a total of {cn(dice_throws)} times\n')
    for i in moveslist:
        out.write(f'{proplist[ct]} was landed on {cn(i)} times and was visited {100*i/float(dice_throws):.{DIGITS}f}% of dice rolls\n')
        ct += 1
    ct = 0
    for i in moveslist:
        if ct != len(proplist)-1:
            #out.write('{}'.format(proplist[ct])+(23-len(proplist[ct]))*' '+'{:.4f}%\n'.format(100*i/float(dice_throws)))
            out.write(f'{proplist[ct]}'+(23-len(proplist[ct]))*' '+f'{100*i/float(dice_throws):.{DIGITS}f}%\n')
            ct += 1
        else:
            out.write(f'{proplist[ct]}'+(23-len(proplist[ct]))*' '+f'{100*i/float(dice_throws):.{DIGITS}f}%')
    out.close()

# Example Usage
# monopoly(10**8,1)
# monopolyw(10**8,1,'10^8_monopoly.txt')

