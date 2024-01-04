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

game_images = [rock, paper, scissors]

if yourchoice > 2 or yourchoice < 0:
    message = "You have entered an invalid number"
else:
    print(game_images[yourchoice])
    print("Computer chose:")    
    print(game_images[pcchoice])

print(message)