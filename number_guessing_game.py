# Number Guessing Game - Viet Hoang Cao 

import random 

while True:
  secret_number = random.randint(1,20)
  tries = 0
  guess = 0

  question = input("Welcome to my number guessing game. Are you ready ?").title().strip()
  if question == "Yes":
    print("Let's get the ball rolling !")
    rule = "You are going to have a total of four tries. Note that your guess must not less than 1 or greater than 20. An incorrect guess will lose you a try" 
    print(rule)
    while secret_number != guess and tries < 4 : 
      guess = int(input("Enter your guess:").strip())
      if guess < 0 or guess > 20:
        print("Your guess is out of range")
        tries += 1                                      
        print(f"tries = {tries}")
      elif guess < secret_number:
        print("The secret number is greater than your guess")
        tries += 1
        print(f"tries = {tries}")
      elif guess > secret_number:
        print("The secret number is less than your guess")
        tries += 1
        print(f"tries = {tries}")
        
    if guess == secret_number:
      print("This is the correct guess. Well done!")
    elif guess != secret_number:
      print(f"Sorry you have no tries left. The secret number is {secret_number}")
  
  elif question == "No":
    print("Okay. Have a great day")
    break
  else:
    print("Invalid input. Try again") 
    continue
    
  replay = input("Do you want to replay ? Yes or No ? ").title().strip()
  if replay == "Yes":
    continue
  elif replay == "No":
    print("Thank you very much for playing my game. See you next time !")  
    break 
