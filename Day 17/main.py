class User:
    def __init__(self, user_id, username):
        print("new user has been created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Dave")
# print(user_1.username)
# print(user_1.follower)

user_2 = User("002", "John")
# user_2.id = "002"
# user_2.username = "John"

# print(user_2.username)

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)

print(user_2.following)
print(user_2.followers)