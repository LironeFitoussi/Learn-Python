from art import logo, vs
from random import choice
from game_data import data


def format_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def get_random_account(previous_account=None):
    account = choice(data)
    while account == previous_account:
        account = choice(data)
    return account


def compare_followers(guess, a, b):
    if a["follower_count"] > b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)
    score = 0
    account_a = get_random_account()
    account_b = get_random_account(account_a)

    while True:
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = compare_followers(guess, account_a, account_b)

        print("\n" * 20)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b
            account_b = get_random_account(account_a)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            print(f"{account_a['name']} has {account_a['follower_count']}M followers")
            print(f"{account_b['name']} has {account_b['follower_count']}M followers")
            break


if __name__ == "__main__":
    play_game()
