# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total_sum += student_heights[n]

avg_height = round(total_sum / len(student_heights))
print(avg_height)