import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_list[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_list[computer_choice]}")

if user_choice == computer_choice:
    print("Draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer win!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer win!")
else:
    print("You win!")