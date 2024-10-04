import random            # python module
import day4_my_module    #call this python module from other file!

random_integer = random.randint(44, 100)
print(random_integer)
# python 2nd module
print(day4_my_module.pi)

random_float = random.random() * 10     # 0.0000000 to 9.9999999......
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")