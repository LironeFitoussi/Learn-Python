# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
# print(student_heights)
total_heights = 0
for height in student_heights:
  total_heights += height
print(f"total height = {total_heights}")

num_of_students = 0
for student in student_heights:
  num_of_students += 1
print(f"number of students = {num_of_students}")


print(f"average height = {round(total_heights / num_of_students)}")
