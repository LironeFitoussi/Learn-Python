import random

user_cards = []
computer_cards = []


def deal_card():
    """
    Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


for _ in range(2):
    # Add two cards to user
    user_cards.append(deal_card())

    # Add two cards to computer
    computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)
