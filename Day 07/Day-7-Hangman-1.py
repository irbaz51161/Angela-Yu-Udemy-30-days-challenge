import random

word_list = ["aardvark", "baboon", "camel"]

#To do-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TO do-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Enter your guess: ").lower()

#To do-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong") 