# Enter your height in meters e.g., 1.55
height = float(input("Please, enter your height in meters: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Please, enter your weight in kilograms: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
  message = "you are underweight."
elif bmi >= 18.5 and bmi < 25:
  message = "you have a normal weight."
elif bmi >= 25 and bmi < 30:
  message = "you are slightly overweight."
elif bmi >= 30 and bmi < 35:
  message = "you are obese."
else:
  message = "you are clinically obese."

print(f"Your BMI is {bmi}, {message}")