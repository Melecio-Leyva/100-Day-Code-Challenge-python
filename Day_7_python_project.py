#Hang man Game

import os
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#import random class
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#List for random choices
word_list = ["aardvark", "baboon", "camel"]

#create random choice from the List
chosen_word = random.choice(word_list)
#print hangman logo
print(logo)
#print the chosen word for debugginng
print(f"psst, the chosen word is {chosen_word}")

#create word length from chosen_word
word_length = len(chosen_word)

#give the user lives
lives  = 6

#create a list to display the missing letters
display =[]

#loop through the chosen word and add underscores to the list. same size as chosen word.
for _ in range(word_length):
    display += "_"

#print the display list
print(display)


#create boolean to check if they have won
end_of_game = False
#create while loop to loop through the display list and check for underscores left
while not end_of_game:
    #takes users input.
    guess = input("Guess a letter").lower()
    cls()
    #if user guess's a letter that he already used the let them know
    if guess in display:
        print("you have already guessed " + guess)
    #Check if the letter is in the random word
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guess letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess} thats not in the word and you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game=True
            print("You lose!")
    #print display after letter guessed
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Won!")
    #print the ascii assert
    print(stages[lives])
