enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# drink_potion()
# print(
#     potion_strength
# )  # This will raise an error because potion_strength is not defined outside the function. It is a local variable.


player_health = 10


def game():
    def drink_potion():
        # This is a local variable and it will not affect the global variable.
        potion_strength = 2
        print(player_health)


drink_potion()  # This will return an error because potion_strength is not defined outside the function.
print(player_health)
