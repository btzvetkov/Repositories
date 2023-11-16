height = int(input("Please, enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please, enter your age: "))
    if age > 18:
        print("Your price is $12")
    elif age >= 12 and age <= 18:
        print("Your price is $7")
    elif age < 12:
        print("Your price is $5")
else:
    print("Sorry, you can't ride the rollercoaster!")