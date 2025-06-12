# auth.py
import hashlib
from storage import load_users, save_users

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password = password_hash

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def create_user(cls, username, password):
        password_hash = cls.hash_password(password)
        return cls(username, password_hash)

    def verify_password(self, password):
        return self.password == self.hash_password(password)


class AuthManager:
    def __init__(self):
        self.users = load_users()

    def register(self, username, password):
        if username in self.users:
            print("❌ Username already exists.")
            return False

        user = User.create_user(username, password)
        self.users[username] = user.password
        save_users(self.users)
        print("✅ User registered successfully!")
        return True

    def login(self, username, password):
        if username not in self.users:
            print("❌ User not found.")
            return False

        user = User(username, self.users[username])
        if user.verify_password(password):
            print("✅ Login successful!")
            return True
        else:
            print("❌ Incorrect password.")
            return False
