# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo = '''
 .oOOOo.                                        o                o.     O                  o                 
.O     o                                       O                 Oo     o                 O                  
o                                          O   o                 O O    O                 O                  
O                                         oOo  O                 O  o   o                 o                  
O   .oOOo O   o  .oOo. .oOo  .oOo          o   OoOo. .oOo.       O   o  O O   o  `oOOoOO. OoOo. .oOo. `OoOo. 
o.      O o   O  OooO' `Ooo. `Ooo.         O   o   o OooO'       o    O O o   O   O  o  o O   o OooO'  o     
 O.    oO O   o  O         O     O         o   o   O O           o     Oo O   o   o  O  O o   O O      O     
  `OooO'  `OoO'o `OoO' `OoO' `OoO'         `oO O   o `OoO'       O     `o `OoO'o  O  o  o `OoO' `OoO'  o     
'''
print(logo)
print("Welcome to the Number Guessin Game!")
print("I'm thinking of a number between 1 - 100")

random_num = random.randint(1,101)
print(f"The answer is {random_num} for debugging.")
choice = input("Choose difficulty. Type 'easy' or 'hard':").lower()

def attempt(choose):
    attempts = 0
    if choose == 'easy':
        attempts = 5
    else:
        attempts = 10
    return attempts

lifes = attempt(choice)
end_loop = True
while end_loop:
    print(f"You have {lifes} attempts left:")
    guess = int(input("Make a guess: "))
    if guess == random_num:
        print("Correct! you win!")
        end_loop = False
    elif guess> random_num:
        lifes = lifes - 1
        print("Too High")
    elif guess < random_num:
        lifes = lifes - 1
        print("Too Low!")
    
    if lifes<0:
        end_loop = False
    