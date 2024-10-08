import random

user_cards = []
computer_cards = []
is_game_over = False


def deal_card():
    """
    Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


for _ in range(2):
    # Add two cards to user
    user_cards.append(deal_card())

    # Add two cards to computer
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
