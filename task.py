import json
import os

TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self, username):
        self.username = username
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """if the file doesn't exit return an empty list """
        if not os.path.exists(TASKS_FILE):
            return []
        """if it exit read all users tasks"""
        with open(TASKS_FILE, "r") as f:
            all_tasks = json.load(f)
            return all_tasks.get(self.username, [])

    def save_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                all_tasks = json.load(f)
        else:
            all_tasks = {}

        all_tasks[self.username] = self.tasks

        with open(TASKS_FILE, "w") as f:
            json.dump(all_tasks, f, indent=4)

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['description']} - {status}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print("✅ Task marked as completed.")
        else:
            print("❌ Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑️ Task '{removed['description']}' deleted.")
        else:
            print("❌ Invalid task number.")
