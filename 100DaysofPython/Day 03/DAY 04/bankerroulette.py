# random gives who will pay the bill by inputing the names of the people separated by comma and space - ", "
import random

names_string = input()
names = names_string.split(", ")

whowillpay = random.randint(0,(len(names)-1))

print(f"{names[whowillpay]} is going to buy the meal today!")

