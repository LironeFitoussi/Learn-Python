# Import the game data and the art
from art import logo, vs
from random import choice
from game_data import data

# Variables
score = 0
is_game_over = False

# Dispaly Art
print(logo)

# Generate Random account from game data
account_a = choice(data)
account_b = choice(data)

while account_a == account_b:
    account_b = choice(data)


# Format account data into printable format
def format_account(account):
    """
    Take the account data and return the printable format
    """
    return f"{account['name']}, a {account['description']}, from {account['country']}"


# Display account data
print(f"Compare A: {format_account(account_a)}")

while not is_game_over:
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    # Ask user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## - Get follower count of each account
    def compare_followers(user_guess, a, b):
        """
        Check if the user guess is correct
        """
        winner = ""
        ## - Use if statement to check if user is correct
        if a["follower_count"] > b["follower_count"]:
            winner = "a"
        else:
            winner = "b"

        return user_guess == winner

    is_correct_guess = compare_followers(user_guess, account_a, account_b)

    def set_winner():
        """
        Set the Highest follower count account as account A
        """
        global account_a, account_b
        if account_a["follower_count"] > account_b["follower_count"]:
            continue
        else:
            account_a = account_b

    def continue_game():
        """
        Continue the game
        """
        set_winner()

        # get new account B
        account_b = choice(data)

        while account_a == account_b:
            account_b = choice(data)

        print(f"Compare A: {format_account(account_a)}")

    # Give user feedback on their guess
    if is_correct_guess:
        print("\n" * 20)
        # score keeping
        score = score + 1
        print("You are correct!")
        # print 20 empty lines
        continue_game()
    elif not is_correct_guess:
        is_game_over = True
        print("You are wrong!")
        # show actual follower count
        print(f"{account_a['name']} has {account_a['follower_count']}M followers")
        print(f"{account_b['name']} has {account_b['follower_count']}M followers")
        print(f"Final Score: {score}")
