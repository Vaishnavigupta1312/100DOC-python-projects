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
game_images = [rock, paper, scissors]
user_choice = int(
    input(
        "What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if (user_choice >= 3 or user_choice < 0):
    print("Invalid choice, You lost!")
else:
    print(game_images[user_choice])
    # if choice==0:
    #   print(rock)
    # elif choice==1:
    #   print(paper)
    # else:
    #   print(scissors)
    print("Computer chose:")
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])
    # if computer_choice==0:
    #   print(rock)
    # elif computer_choice==1:
    #   print(paper)
    # else:
    #   print(scissors)

    if user_choice == 1 & computer_choice == 3:
        print("You won")
    elif user_choice == 2 & computer_choice == 1:
        print("You won")
    elif user_choice == 3 & computer_choice == 1:
        print("You won")
    elif user_choice == computer_choice:
        print("It's a draw")
    else:
        print("You lost")
