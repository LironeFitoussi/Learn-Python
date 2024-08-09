hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---
    """,  # Stage 1: The initial state, only the gallows.

    """
     ------
     |    |
     |    O
     |
     |
     |
    ---
    """,  # Stage 2: Head added.

    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    """,  # Stage 3: Body added.

    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    """,  # Stage 4: One arm added.

    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---
    """,  # Stage 5: Second arm added.

    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---
    """,  # Stage 6: One leg added.

    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """  # Stage 7: Full figure, game over.
]
