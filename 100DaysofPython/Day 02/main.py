#Data Types
# 1st input: enter height in meters e.g: 1.65
height = float(input("Please, enter your height: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Please, enter your weight: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = height/(weight ** 2)
# print(type(height))
# print(type(weight))
bmi_final = round(bmi, 2)
print(bmi_final)