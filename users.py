class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"User(username='{self.username}', role='{self.role}')"

def requires_role(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role == required_role:
                return func(user, *args, **kwargs)
            else:
                return f"\n ! Access denied. {user.username} is not {required_role}."
        return wrapper
    return decorator

def user_filter(users, role):
    for user in users:
        if user.role == role:
            yield user

users = [
    User("A", "admin"),
    User("B", "editor"),
    User("C", "editor"),
    User("D", "viewer"),
    User("E", "viewer")
]

@requires_role("admin")
def adminsmth(user):
    return f"\nAdmin {user.username} made something "

@requires_role("editor")
def edit(user):
    return f"\n{user.username} Edited something"

print(adminsmth(users[0]))  
print(adminsmth(users[2]))  
print(edit(users[2]))  
print(edit(users[4]))  


filtered_admins = user_filter(users, "admin")
print("\nList of admins:", list(filtered_admins))

filtered_editors = user_filter(users, "editor")
print("List of editors:", list(filtered_editors))

filtered_viewers = user_filter(users, "viewer")
print("list of viewers:", list(filtered_viewers))


