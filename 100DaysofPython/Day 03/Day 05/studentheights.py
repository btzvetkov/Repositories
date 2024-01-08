# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sumup = 0
for i in student_heights:
    sumup += i

average_thing = round((sumup / len(student_heights)))

print(f"total height = {sumup}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {average_thing}")