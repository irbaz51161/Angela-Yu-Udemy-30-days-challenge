import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
random_name = names[random_choice]
print(f"{random_name} is going to buy the meal today!")