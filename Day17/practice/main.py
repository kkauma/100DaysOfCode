# OOP and creating classes in Python
# Init is called for every instance a class that gets created

class User:
    def __init__(self, employee_id, username):
        self.employee_id = employee_id
        self.username = username


user1 = User("001", "Ace")

print(f"The employee's username is {user1.username}, and their id is {user1.employee_id}.")