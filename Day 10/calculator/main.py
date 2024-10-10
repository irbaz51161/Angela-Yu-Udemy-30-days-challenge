# ✅ TODO 01 - Import logo from art.py and print it
# ✅ TODO 02 - Take a number to start calculating and then ask the symbol which we will store in a 'Docstring' then we will ask the 2nd integer and will use if - else

from art import logo

def solve(num1, symb, num2):
    if symb == "+":
        return num1 + num2
    elif symb == "-":
        return num1 - num2
    elif symb == "/":
        return num1 / num2
    elif symb == "*":
        return num1 * num2
    elif symb == "//":
        return num1 // num2
    elif symb == "%":
        return num1 % num2
    elif symb == "**":
        return num1 ** num2
    else:
        return "Invalid symbol!"

print(logo)
stop_loop = True
number_1 = int(input("Enter the number: "))
while stop_loop:
    symbol = input("""Enter one of the following symbol:
                +
                -
                /
                *
                //
                %
                ** """)
    number_2 = int(input("Enter the number again: "))
    s = solve(number_1, symbol, number_2)
    print(f"The output is: {number_1} {symbol} {number_2} = {s}")
    number_1 = s
    choice = input("Do you want to solve further with this input? Type 'yes' for further calculations or type 'no' to stop it: ").lower()
    if choice == "yes":
        print(f"The previous number is {s}")
    else:
        stop_loop = False

    