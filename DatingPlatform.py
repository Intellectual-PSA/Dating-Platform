class UserProfile:
    def __init__(self, name, age, location, interests):
        self.name = name
        self.age = age
        self.location = location
        self.interests = interests

class DatingPlatform:
    def __init__(self):
        self.users = []

    def add_user(self, name, age, location, interests):
        new_user = UserProfile(name, age, location, interests)
        self.users.append(new_user)
        print(f"User {name} added to the platform.")

    def search_users_by_interest(self, interest):
        matches = [user for user in self.users if interest in user.interests]
        return matches

# Sample usage
if __name__ == "__main__":
    dating_platform = DatingPlatform()

    dating_platform.add_user("Alice", 30, "New York", ["Reading", "Music", "Sports"])
    dating_platform.add_user("Bob", 35, "Chicago", ["Art", "Sports", "Travel"])
    dating_platform.add_user("Charlie", 28, "Los Angeles", ["Music", "Movies", "Travel"])

    print("Searching users interested in 'Sports':")
    for user in dating_platform.search_users_by_interest("Sports"):
        print(f"Name: {user.name}, Age: {user.age}, Location: {user.location}, Interests: {', '.join(user.interests)}")
