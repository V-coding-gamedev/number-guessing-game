# Number Guessing Game - Viet Hoang Cao 

import random

secret_number = random.randint(1,20)

def number_guessing_game():
    tries = 0 
    ans = 0
    question = "What is the number of books that I bought yesterday ? "

    print("Welcome to my number guessing game!")
    ready = input("Are you ready ? ").strip().title()
    if ready == 'Yes':
        print(f"Then let's get the ball rolling")
        print(f"You are going to have a total of four gueeses")
        print(question)

        while tries < 4 and ans != secret_number:
            ans = int(input("The total number of books that I bought yesterday is:").strip())
            if ans < 1 or ans > 20: # check range first before check higher and lower
                print(f"The number you entered is out of range. Please, try again !")
                tries = tries + 1 
            elif ans < secret_number:
                print(f"The answer is greater than your guess. Please, try again !")
                tries = tries + 1 
            elif ans > secret_number:
                print(f"The answer is lower than your guess. Please, try again !")
                tries = tries + 1 

        if ans == secret_number:
            print(f"Congratulations, you have done a great job")
        else:    
            print(f"No more guesses, the answer is {secret_number}")

    elif ready == 'No':
        print(f"Then see you next time")
    else:
        print(f"Invalid text! Please only enter yes or no")    

while True:
    number_guessing_game()
    replay = input("Do you want to start over ?").title().strip()
    if replay == "No":
        break
    elif replay == "Yes":
        continue