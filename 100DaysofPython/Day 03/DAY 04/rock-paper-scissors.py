import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

yourchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

pcchoice = random.randint(0,2)

if (yourchoice == 0 and pcchoice == 1) or (yourchoice == 1 and pcchoice == 2) or (yourchoice == 2 and pcchoice == 0):
    message = "You lose"
elif (yourchoice == 0 and pcchoice == 2) or (yourchoice == 1 and pcchoice == 0) or (yourchoice == 2 and pcchoice == 1):
    message = "You win"
else:
    message = "Draw"

if yourchoice == 0:
    print(rock)
elif yourchoice == 1:
    print(paper)
elif yourchoice == 2:
    print(scissors)

print("Computer chose:")    
if pcchoice == 0:
    print(rock)
elif pcchoice == 1:
    print(paper)
elif pcchoice == 2:
    print(scissors)

print(message)
# print(f"The computer chose {pcchoice}")
