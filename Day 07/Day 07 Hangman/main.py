#importing files and variables + random
import random
from hangman_art import stages
from hangman_art import logo
from hangman_words_list import word_list


chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)
lives = 6
game_end = False
stages_i = 6

#making an empty guess list
display = []
for i in chosen_word:
    display.append("_")
print(chosen_word)
#Printing Logo and taking guess
print(logo,"\n\n")
print(" ".join(display))

while not game_end:
    guess = input("Enter your guess: ").lower()

    for i in range(len_chosen_word):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    print(" ".join(display))

    if "_" not in display:
        print("You Win!")
        game_end = True
    if guess not in chosen_word:
        lives -= 1
        stages_i -=1
        print(stages[stages_i])
        if lives == 0:
            print("You lose. Game Over!")
            game_end = True


display = " ".join(display)
print(f"Your output is: {display}")
print(f"The word was: {chosen_word}")