import json
import os

USER_DATA_FILE = "users.json"

def load_users():
    """Load users from the jsoon file"""
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, 'r') as file:
     try:
        return json.load(file)
     except json.JSONDecodeError:
        return {}
def save_users(users):
    """Save users to the json file"""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)
        