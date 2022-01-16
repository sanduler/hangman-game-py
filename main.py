# Name: Ruben Sanduleac
# Date: January 16th, 2022

# user the random libary to be able to randomly select a word
import random


word_list = ["aardvark", "baboon", "camel", "yummy", "zigzagging",
             "wristwatch", "razzmatazz", "kilobyte", "stronghold"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# check if the random word was chosen
# print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
