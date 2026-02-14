import random
import time

''' PRE-DEFINED SETS and VARIABLES '''
#don't use nested dict, just build classes for things like this
playerStats = {
    'PlayerX' : {
        'tier' : 1,
        'wealth' : 5,
        'food' : 1,
        'militaryStr' : 0,
        'foodProd' : 0
    },

    'PlayerY' : {
        'tier' : 1,
        'wealth' : 5,
        'food' : 1,
        'militaryStr' : 0,
        'foodProd' : 0
    }
}

'''Status Update Functions'''
#should have caught this one... extremely repetitive, use 'tier' to add to wealth/food, and math to describe promotions
def statUpdates(player):
    match playerStats[player]["tier"]:
        case 1:
            if playerStats[player]["food"] >= 4:
                playerStats[player]["tier"] += 1
                if player == 'PlayerX':
                    time.sleep(0.2)
                    print(f"Your kingdom grew in size! You now gain +2 food and +2 wealth after each round. For tier 3 you will need 8 food.")
                playerStats[player]["wealth"] += 2
                playerStats[player]["food"] += playerStats[player]["foodProd"]
            else:
                playerStats[player]["wealth"] += 1
                playerStats[player]["food"] += 1
                playerStats[player]["food"] += playerStats[player]["foodProd"]
        case 2:
            if playerStats[player]["food"] >= 8:
                playerStats[player]["tier"] += 1
                playerStats[player]["food"] -= 1
                if player == 'PlayerX':
                    time.sleep(0.2)
                    print(f"Your kingdom grew in size! You now gain +3 food and +3 wealth after each round. For tier 4 you will need 16 food.")
                playerStats[player]["wealth"] += 3
                playerStats[player]["food"] += playerStats[player]["foodProd"]
            else:
                playerStats[player]["wealth"] += 2
                playerStats[player]["food"] += 2
                playerStats[player]["food"] += playerStats[player]["foodProd"]
        case 3:
            if playerStats[player]["food"] >= 16:
                playerStats[player]["tier"] += 1
                playerStats[player]["food"] -= 4
                if player == 'PlayerX':
                    time.sleep(0.2)
                    print(f"Your kingdom grew in size! You now gain +4 food and +4 wealth after each round. For tier 5 you will need 32 food.")
                playerStats[player]["wealth"] += 4
                playerStats[player]["food"] += playerStats[player]["foodProd"]
            else:
                playerStats[player]["wealth"] += 3
                playerStats[player]["food"] += 3
                playerStats[player]["food"] += playerStats[player]["foodProd"]
        case 4:
            if playerStats[player]["food"] >= 32:
                playerStats[player]["tier"] += 1
                playerStats[player]["food"] -= 11
                if player == 'PlayerX':
                    time.sleep(0.2)
                    print(f"Your kingdom grew in size! You have gained +5 food and +5 wealth. Survive the next round and you win!")
                playerStats[player]["wealth"] += 5
                playerStats[player]["food"] += playerStats[player]["foodProd"]
            else:
                playerStats[player]["wealth"] += 4
                playerStats[player]["food"] += 4
                playerStats[player]["food"] += playerStats[player]["foodProd"]

'''Computer Movement'''
def getComputerChoice():
     choiceValue = random.random()
     if choiceValue < 3/10 and playerStats["PlayerY"]["wealth"] >= 1:
        if playerStats["PlayerY"]["wealth"] >= 5:
            playerStats["PlayerY"]["foodProd"] += 1
            playerStats["PlayerY"]["wealth"] -= 5
        else:
            playerStats["PlayerY"]["militaryStr"] += 1
            playerStats["PlayerY"]["wealth"] -= 1
     else:
        compAtk = attackSim('PlayerY')
        playerDef = attackSim('PlayerX')
        if compAtk > playerDef:
            playerStats["PlayerY"]["tier"] += 1
            playerStats["PlayerX"]["tier"] -= 1
            if playerStats["PlayerX"]["tier"] == 0:
                playerStats["PlayerX"]["tier"] += 1
            time.sleep(0.2)
            print(f"Oof! The other player decimated you! You are now tier {playerStats['PlayerX']['tier']} and PlayerY is tier {playerStats['PlayerY']['tier']}")
        else:
            time.sleep(0.2)
            print(f"You thwarted off the other players attack for now...")

'''Player Options'''
def mainMenu():
    while True:
        time.sleep(0.2)
        choicePlayer = input("Do you want to spend wealth or attack the enemy?\n")
        #.lower can be added directly to input() like I had thought...
        if choicePlayer.lower() == "spend":
            playerChoice = getPlayerChoice('spend')
            if playerChoice == 'back':
                continue
            else: break
        elif choicePlayer.lower() == "attack":
            playerChoice = getPlayerChoice('attack')
            if playerChoice == 'back':
                continue
            else: break
        elif choicePlayer.lower() == "quit":
            quit()
        else:
            time.sleep(0.2)
            print(f"That was not a valid input, please enter either 'spend' or 'attack'")
            continue

def getPlayerChoice(choice):
    if choice.lower() == "spend":
        while True:
            time.sleep(0.2)
            choicePlayer = input("Do you want to spend: [1] 5 wealth to increase food production, or [2] 1 wealth to increase your military strength?\n")
            if choicePlayer.lower() == "1" and playerStats["PlayerX"]["wealth"] >= 5:
                playerStats["PlayerX"]["foodProd"] += 1
                playerStats["PlayerX"]["wealth"] -= 5
                time.sleep(0.2)
                print(f"You've increased your food production by 1! You now produce +{playerStats['PlayerX']['foodProd']} food each turn!")
                break
            elif choicePlayer.lower() == "1" and playerStats["PlayerX"]["wealth"] < 5:
                time.sleep(0.2)
                print(f"Sorry, you don't have enough wealth to do that. Please choose something else.")                    
                continue
            elif choicePlayer.lower() == "2" and playerStats["PlayerX"]["wealth"] >= 1:
                playerStats["PlayerX"]["militaryStr"] += 1
                playerStats["PlayerX"]["wealth"] -= 1
                time.sleep(0.2)
                print(f"You've increased your military strength by 1! The total strength added to each roll is now {playerStats['PlayerX']['militaryStr']}!")
                break
            elif choicePlayer.lower() == "2" and playerStats["PlayerX"]["wealth"] == 0:
                time.sleep(0.2)
                print(f"Sorry, you don't have enough wealth to do that. Please choose something else.")
                continue
            elif choicePlayer.lower() == "back":
                return 'back'
            else:
                time.sleep(0.2)
                print(f"That was not a valid input, please enter either '1' or '2', or say 'back' to go back.")
                continue
    elif choice.lower() == "attack":
        time.sleep(0.2)
        print(f"You currently have a +{playerStats['PlayerX']['militaryStr']} to your attack rolls. Do you want to roll against Player Y? (y/n)\n")
        while True:
            choicePlayer = input()
            if choicePlayer.lower() == "y" :
                playerAtk = attackSim('PlayerX')
                compDef = attackSim('PlayerY')
                if playerAtk > compDef:
                    playerStats["PlayerX"]["tier"] += 1
                    playerStats["PlayerY"]["tier"] -= 1
                    if playerStats["PlayerY"]["tier"] == 0:
                        playerStats["PlayerY"]["tier"] += 1
                    time.sleep(0.2)
                    print(f"Congratulations! Your offensive overpowered the other player! You are now tier {playerStats['PlayerX']['tier']} and PlayerY is tier {playerStats['PlayerY']['tier']}")
                else:
                    time.sleep(0.2)
                    print(f"The other player thwarted off your attack... maybe next time...")
                break
            elif choicePlayer.lower() == "n":
                return 'back'
            else:
                time.sleep(0.2)
                print(f"That was not a valid input, please enter either 'y' to attack or 'n' to go back.")
                continue
    else:
        time.sleep(0.2)
        print(f"You should theoretically not see this text... theoretically.")
                
'''Attack Roll'''
def attackSim(player):
    roll = random.randint(1, 6)
    atkStrength = roll + playerStats[player]["militaryStr"]
    #return roll, atkStrength - not necessary but could be helpful/descriptive
    return atkStrength

'''Game rounds'''
def mainloop():
    while playerStats['PlayerX']["tier"] < 5 and playerStats['PlayerY']["tier"] < 5:
        time.sleep(0.2)
        print("\nYour move...")
        mainMenu()
        time.sleep(0.2)
        print(f"PlayerY is making their move...")
        getComputerChoice()
        if playerStats['PlayerX']["tier"] == 5:
            return 'PlayerX'
        elif playerStats['PlayerY']["tier"] == 5:
            return 'PlayerY'
        else:
            statUpdates('PlayerX')
            statUpdates('PlayerY')
            time.sleep(0.2)
            print(f"Your stats are now: \n\
            Tier: {playerStats['PlayerX']['tier']}\n\
            Wealth: {playerStats['PlayerX']['wealth']}\n\
            Food: {playerStats['PlayerX']['food']}\n\
            Military Strength: +{playerStats['PlayerX']['militaryStr']}")
            print(f"PlayerY is currently a tier {playerStats['PlayerY']['tier']} kingdom...")
            continue

'''Basic Set-up'''
def main():
    print(f"Welcome to X v Y, a simple strategy game of where both players race to become the strongest by developing, earning more resources, and attacking the opposing player. Be the first to tier 5 to win! You'll go first...")
    #text delay could be changed to a variable to easily adjust delay to all occurrences
    time.sleep(0.2)
    print(f"Your current stats are \n\
        Tier: {playerStats['PlayerX']['tier']}\n\
        Wealth: {playerStats['PlayerX']['wealth']}\n\
        Food: {playerStats['PlayerX']['food']}\n\
        Military Strength: +{playerStats['PlayerX']['militaryStr']}")
    winner = mainloop()
    time.sleep(0.2)
    print(f"{winner} reached tier 5 first! {winner} wins!")

'''Execute game'''
if __name__ == "__main__":
    main()            
