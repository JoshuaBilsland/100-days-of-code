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
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice not in [0,1,2]:
    print("Invalid choice")
else: 
    computer_choice = random.randint(0, 2)
    print()
    option_ascii_art = [rock, paper, scissors]
    print(option_ascii_art[user_choice])
    print("Computer Chose:\n")
    print(option_ascii_art[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw")
        
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")

    elif user_choice == 1 and computer_choice == 2:
        print("You lost")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")

    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")