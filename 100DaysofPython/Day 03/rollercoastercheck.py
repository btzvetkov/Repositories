height = int(input("Please, enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please, enter your age: "))
    if age > 18:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age < 12:
        bill = 5
        print("Child tickets are $5")
    
    whants_photo = input("Do you want a photo taken? Y or N.")
    if whants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you can't ride the rollercoaster!")
