student_scores = input("Input a list of student scores: ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

total_even = 0

for k in student_scores:
    if k % 2 == 0:
        total_even += k
    
print(f"Sum of total even numbers is: {total_even}")