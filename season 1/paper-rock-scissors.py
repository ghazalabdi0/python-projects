
#paper rock scissors game
import random

#constants and variables
choices = ("rock", "paper" , "scissors")  #tupple 

#get the user choice
def getUserChoice():
    userChoice= input("select yourchoice from : rock, paper, scissors: ")
    while userChoice not in choices:
       userChoice= input("select yourchoice from : rock, paper, scissors: ")
    return userChoice

#generate the PC choice
def generateMachineChoice():
    machineChoice = random.choice(choices)
    return machineChoice

#determine the winner
def determineWinner(machineChoice, userChoice, machineCount, userCount):
    print("PC has just chosen:", machineChoice)
    if (machineChoice == "rock" and userChoice == "scissors") or (machineChoice == "scissors" and userChoice == "paper") or (machineChoice == "paper" and userChoice == "rock"):
            machineCount = machineCount + 1 
    elif(machineChoice ==  userChoice):
            determineWinner(generateMachineChoice(), getUserChoice(), machineCount, userCount)
    else:
            userCount = userCount+1
       
#general function to run the code
def generalFunction():
    machineCount = 0
    userCount = 0
    for i in range(0,2):
        determineWinner(generateMachineChoice(), getUserChoice(), machineCount, userCount)
    print("===]0=]0][oluhlul,hjk,jkk]", machineCount, userCount)
    if (machineCount > userCount) :
        print("OOOOOps, you lost!!!!!")
    else:
        print("**WOoooooooooow, you win**")

#run & irritation
generalFunction()
while input("do you want to continue? (y/n): ") == "y":
    generalFunction()