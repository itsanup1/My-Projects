import random as rd

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
lst = [rock, paper, scissors]
print("WELCOME TO THE ROCK PAPER SCISSORS! ")

choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n=>"))

print(f'''\nYou Chose:
    {lst[choice]}''')
    
comp = rd.randint(0,2)
print(f'''\nComputer Chose:
    {lst[comp]}''')

print("\nRESULT:\n")

if choice == 0 and comp == 1:
    print("You Lose!") 
if choice == 0 and comp == 2:
    print("You Won!")
if choice == 1 and comp == 0:
    print("You Won!")   
if choice == 1 and comp == 2:
    print("You Lose!")
if choice == 2 and comp == 0:
    print("You Lose!")         
if choice == 2 and comp == 1:
    print("You Won!")    
if choice == comp:
    print("It's a DRAW!")    