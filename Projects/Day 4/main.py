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
game_images = [rock, paper, scissors]

user_choise = int(input("What Do you Choose? Type 0 for Rock 1 for Paper or 2 for scissors. \n"))
if user_choise > 2 or user_choise < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choise])
    comp_choise = random.randint(0, 2)
    print(f"Computer chose: \n {game_images[comp_choise]}")

    if user_choise == 0 and comp_choise == 2 or user_choise > comp_choise:
        print("You win!")
    elif comp_choise > user_choise or comp_choise == 0 and user_choise == 2:
        print("You lose")
    elif comp_choise == user_choise:
        print("It's a draw!")
    else:
        print("You typed an invalid number, you lose!")