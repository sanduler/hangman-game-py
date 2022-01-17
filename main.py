# Name: Ruben Sanduleac
# Date: January 16th, 2022
# Description: Hangman game, uses OOP to import the dictionary and UI. The game randomly selects a word from the dictionary and gives
#              the user 6 tries to guess the word by inputing a letter. The game give the user feedback on which charecter was typed.

# user the random libary to be able to randomly select a word
import random
import hangman_ui
import dictionary

print(hangman_ui.logo)
print("\n")
# boolian to continue the game
game_continue = True

# Variable called 'lives' to keep track of the number of lives left and set 'lives' to equal 6.
lives = 6

# Randomly choose a word from the word_list function from the dictionary.py
chosen_word = random.choice(dictionary.word_list)


# Check if the random word was chosen
print(f"The solution is {chosen_word}")

# If the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

# Get the size of the word
size = len(chosen_word)

# Create placeholders based on the size of the word
for length in range(size):
    display.append("_")

# Use a while loop to let the user guess again.
# The loop only stops once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
while game_continue:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")

    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for possition in range(size):
        letter = chosen_word[possition]
        if letter == guess:
            display[possition] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You loose a life.")
        lives -= 1
        if lives == 0:
            game_continue = False
            print("You lose.")
    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    # If lives goes down to 0 then the game stops and it prints "You lose."

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(hangman_ui.stages[lives])
    # check if placekeeper underscore is in the list, if not break the while loop
    if '_' not in display:
        game_continue = False
        print("You win!")
