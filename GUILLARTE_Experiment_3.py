import random, os

# Initialize of variables
trials = 0
inMain = True

# Main UI loop
while True:
    print("Choose difficulty:")
    print("[1] Easy (1-20)")
    print("[2] Normal (1-60)")
    print("[3] Hard (1-130)")
    print("[4] Insane (1-400)")
    print("[5] Impossible (1-1000)")
    print()
    
    # Detect error in input
    try:
        option = int(input("Type option: "))
        os.system("CLS")
        if option == 1:
            randInteger = random.randint(1, 20)
            print("Easy Mode selected (1-20)")
            break
        elif option == 2:
            randInteger = random.randint(1, 60)
            print("Normal Mode selected (1-60)")
            break
        elif option == 3:
            randInteger = random.randint(1, 130)
            print("Hard Mode selected (1-130)")
            break
        elif option == 4:
            randInteger = random.randint(1, 400)
            print("Insane Mode selected (1-400)")
            break
        elif option == 5:
            randInteger = random.randint(1, 1000)
            print("Impossible Mode selected (1-1000)")
            break
        else:
            # Run when integer but wrong option
            print("Invalid input!")
            input("Press Enter to continue...")
    except:
        # Run when not integer
        print("Invalid Input!")
        input("Press Enter to continue...")

# Actual game loop
while trials <= 11:
    trials += 1
    
    # Lose condition
    if trials == 11:
        print("You lost, the correct number is {}".format(randInteger))
        break
    try:
        guess = int(input("Guess the number: "))
        if guess == randInteger: # Win condition
            print("Congratulations, you have guessed the correct number ({})!".format(randInteger))
            print("Number of trials: {}".format(trials))
            break
        elif guess < randInteger: # Hint conditions
            print("The number is too low, try again")
        else:
            print("The number is too high try again") 
    except:
        print("Invalid input! +1 trial")
        
print()
input("Press Enter to exit...")
