# There is no block scope in Python.

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(
    new_enemy
)  # This will not raise an error because new_enemy is defined in the global scope.


def create_enemy():
    new_enemy2 = ""
    if game_level < 5:
        new_enemy2 = enemies[0]

    print(
        new_enemy2
    )  # This will raise an error because new_enemy2 is defined in the local scope of the create_enemy() function.
