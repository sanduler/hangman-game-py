# Name: Ruben Sanduleac
# Date: January 16th, 2022

# user the random libary to be able to randomly select a word
import random

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


word_list = ["aardvark", "baboon", "camel", "yummy", "zigzagging",
             "wristwatch", "razzmatazz", "kilobyte", "stronghold"]

# boolian to continue the game
game_continue = True

# Create a variable called 'lives' to keep track of the number of lives left and set 'lives' to equal 6.
lives = 6

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)


# check if the random word was chosen
print(f"The solution is {chosen_word}")


# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

size = len(chosen_word)

for length in range(size):
    display.append("_")

# print(display)
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

while game_continue:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # check if the letter is lower case
    # print(guess)

    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for possition in range(size):
        letter = chosen_word[possition]
        if letter == guess:
            display[possition] = letter

    if guess not in chosen_word:
        lives -= 1
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(stages[lives])
    # check if placekeeper underscore is in the list, if not break the while loop
    if '_' not in display or lives == 0:
        break
