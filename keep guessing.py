from random import randrange

def higher_or_lower():
  
  random_num = randrange(11)

  user_guess = int(input("Pick a number from 1-10: "))

  while user_guess != random_num:

    user_guess = int(input("Pick again: "))
    
    if (user_guess > random_num):
      print("Too high, guess again.") 
    
    if (user_guess < random_num):
      print("Too low, guess again.")
    
    if (user_guess == random_num): 
      print("Correct!")

    
    
higher_or_lower()