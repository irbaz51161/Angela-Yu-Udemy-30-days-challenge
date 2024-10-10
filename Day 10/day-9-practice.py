def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't enter an invalid input."
    f = f_name.title()
    l = l_name.title()
    return f, l

output = format_name(input("1st name: "), input("2nd name: "))
print(output)