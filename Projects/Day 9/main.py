from art import logo

bids_dico = {}
other_players = True

print(logo)
print("Welcome to the secret auction program.")

while other_players:
    # Ask the user for input
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: "))  # Convert the bid to an integer

    # Save data into dictionary {name: price}
    bids_dico[user_name] = user_bid

    # Check if new bids need to be added
    forward = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if forward == 'yes':
        print('\n' * 20)
    else:
        other_players = False

# Get the key with the highest value in the dictionary
winner = max(bids_dico, key=bids_dico.get)

print(f"The winner is {winner} with an amount of ${bids_dico[winner]}")
