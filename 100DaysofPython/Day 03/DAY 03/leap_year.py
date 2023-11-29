# Which year do you want to check?
year = int(input("Please, enter a year to check if it is a leap year or not: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)

if year % 4 == 0:
  if year % 100 > 0:
    print("Leap year")
  elif year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
else:
  print("Not leap year")