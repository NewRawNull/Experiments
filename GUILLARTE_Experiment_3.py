import random, os

trials = 0
inMain = True

def easyMode():
    winNumber = random.randint(1, 15)
    return winNumber
    
def normalMode():
    winNumber = random.randint(1, 40)
    return winNumber
 
def hardMode():
    winNumber = random.randint(1, 85)
    return winNumber
  
def insaneMode():
    winNumber = random.randint(1, 140)
    return winNumber
   
def impossibleMode():
    winNumber = random.randint(1, 300)
    return winNumber

while inMain == True:
    print("Choose difficulty:")
    print("[1] Easy (1-15)")
    print("[2] Normal (1-40)")
    print("[3] Hard (1-85)")
    print("[4] Insane (1-140)")
    print("[5] Impossible (1-300)")
    print()
    try:
        option = int(input("Type option: "))
        os.system("CLS")
        if option == 1:
            randInteger = easyMode()
            print("Easy Mode selected (1-15)")
            inMain = False
        elif option == 2:
            randInteger = normalMode()
            print("Normal Mode selected (1-40)")
            inMain = False
        elif option == 3:
            randInteger = hardMode()
            print("Hard Mode selected (1-85)")
            inMain = False
        elif option == 4:
            randInteger = insaneMode()
            print("Insane Mode selected (1-140)")
            inMain = False
        elif option == 5:
            randInteger = impossibleMode()
            print("Impossible Mode selected (1-300)")
            inMain = False
        else:
            print("Invalid input!")
            input("Press Enter to continue...")
    except:
        print("Invalid Input!")
        input("Press Enter to continue...")

    
    

while trials <= 11:
    trials += 1
    if trials == 11:
        print("You lost, the correct number is {}".format(randInteger))
        break
    try:
        guess = int(input("Guess the number: "))
        if guess == randInteger:
            print("Congratulations, you have guessed the correct number!")
            print("Number of trials: {}".format(trials))
            break
        elif guess < randInteger:
            print("The number is too low, try again")
        else:
            print("The number is too high try again") 
    except:
        print("Invalid input! +1 trial")
        
print()
input("Press Enter to exit...")
