# OOP and creating classes in Python
# Init is called for every instance a class that gets created

# User class built with OOP, add methods and attributes
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def say_hi(self):
        return f"Hello, {self.username}! Welcome to the metaverse."

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Ace")
user2 = User("002", "Python")

user1.follow(user2)
print(user1.say_hi())
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
