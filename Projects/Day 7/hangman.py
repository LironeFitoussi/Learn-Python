import random
from words_module import word_list
from stages import hangman_stages

# Initialize game variables
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
blank_word = "_" * len(chosen_word)
lives_left = 6
letters_guessed = []

def update_blank_word(ch):
    """Update the blank_word with the guessed letter."""
    global blank_word
    new_word_list = list(blank_word)
    for i, ltr in enumerate(chosen_word):
        if ltr == ch:
            new_word_list[i] = ltr
    blank_word = "".join(new_word_list)

def check_final_word():
    """Check if the player has won the game."""
    if "_" not in blank_word:
        print("You won!")
        exit()  # Exit the script if the player wins

def remove_points():
    """Reduce lives and check if the player has lost."""
    global lives_left
    lives_left -= 1
    if lives_left == 0:
        print("You lost!")
        exit()  # Exit the script if the player loses
    print(hangman_stages[abs(lives_left - 6)])

def display_status():
    """Print the current game status."""
    print(hangman_stages[abs(lives_left - 6)])
    print(f"Your Current Guess: {blank_word}")

# Run the Hangman game loop
print("Welcome to Hangman Game!")
print("""
          _______  _        _______  _______  _______  _        _         
|\     /|(  ___  )( (    /|(  ____ \(       )(  ___  )( (    /|( (    /|  
| )   ( || (   ) ||  \  ( || (    \/| () () || (   ) ||  \  ( ||  \  ( |  
| (___) || (___) ||   \ | || |      | || || || (___) ||   \ | ||   \ | |  
|  ___  ||  ___  || (\ \) || | ____ | |(_)| ||  ___  || (\ \) || (\ \) |  
| (   ) || (   ) || | \   || | \_  )| |   | || (   ) || | \   || | \   |  
| )   ( || )   ( || )  \  || (___) || )   ( || )   ( || )  \  || )  \  |  
|/     \||/     \||/    )_)(_______)|/     \||/     \||/    )_)|/    )_)  
                                                                          
by Fistuk                                                                      
""")
while True:
    display_status()
    guess = input("Please guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue
    
    if guess in letters_guessed:
        print("Already tried this one...")
        continue

    letters_guessed.append(guess)

    if guess in chosen_word:
        update_blank_word(guess)
        print("Good job!")
        check_final_word()
    else:
        print("Nope...")
        remove_points()
