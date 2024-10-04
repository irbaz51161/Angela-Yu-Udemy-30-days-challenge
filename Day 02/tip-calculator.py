print('Welcome to the tip calculator.')
bill = float(input("What was the total bill? $"))
people_bill_split = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = bill * (percentage/100)
total_bill = tip + bill
each_pay = total_bill / people_bill_split
print(f"Each person should pay: ${round(each_pay, 2)}")  #OR final_amount = round(bill_per_person, 2)