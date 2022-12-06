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

#Write your code below this line 👇
game_pic = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(game_pic[user_choice])

comp_choice = random.randint(0,2)
print("Computer chose: ")
print(game_pic[comp_choice])

if user_choice >=3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and comp_choice == 2:
  print("You win!")
elif user_choice == 1 and comp_choice == 2:
  print("You lose.")
elif user_choice > comp_choice :
  print("You win!")
elif comp_choice > user_choice :
  print("You lose.")
elif comp_choice == user_choice :
  print("It's a draw.")
