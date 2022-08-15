import random

print("""
  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/          

""")
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100")
random_number = random.randint(1,100) # device is taking a random number
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : \t")

lives = 5
if (difficulty == "hard"):
    print(f"you have {lives} attempts remaining to guess the number \n")
else:
    print(f"you have {lives+5} attempts remaining to guess the number \n")
    lives = 10 # if the difficulty is easy, user will get 10 attempts to guess the number
for i in range(0, lives):
    user_guess = int(input("Make a guess : \t"))

    if(user_guess < random_number):
        print("TOO LOW")
        lives -= 1 # decrease lives by 1
        print(f"you have {lives} attempts remaining to guess the number \n")
    elif (user_guess > random_number):
        print("TOO HIGH")
        lives -= 1
        print(f"you have {lives} attempts remaining to guess the number \n")
    elif (user_guess == random_number):
        print("YOU'VE WON!!!")
        break # get out of the loop

print("GAME OVER")
