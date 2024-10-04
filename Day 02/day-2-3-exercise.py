# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left_years = 90 - int(age)
left_days = 365 * left_years
left_weeks = 52 * left_years
left_months = 12 * left_years

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")