from art import logo
import random

print(logo)

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Set the number of attempts based on difficulty level
    if level_choice == "easy":
        attempts = EASY_LEVEL_TURNS
    elif level_choice == "hard":
        attempts = HARD_LEVEL_TURNS
    else:
        print("Invalid input.")
        return

    user_guess = 0

    while user_guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess > number:
            print("Too high.")
        elif user_guess < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}.")
            return

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return


game()
