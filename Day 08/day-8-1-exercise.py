import math
def main():

    def no_of_cans(wall_height, wall_width):
        total_cans = (wall_height * wall_width) / 5
        print(f"Total cans required are {math.ceil(total_cans)}")

    w_height = int(input("Enter the height of the wall: "))
    w_width = int(input("Enter the width of the wall: "))
    no_of_cans(w_height, w_width)

main()