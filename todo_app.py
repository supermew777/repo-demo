class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

        tasks_list = []

import json

def save_to_file():
    data = [{"desc": t.description, "done": t.is_completed} for t in tasks_list]
    with open("my_tasks.json", "w") as file:
        json.dump(data, file)

while True:
    print("\n1. Add Task | 2. View Tasks | 3. Exit")
    choice = input("Select: ")

    if choice == "1":
        name = input("Enter task: ")
        new_task = Task(name)
        tasks_list.append(new_task) 
        save_to_file()
    elif choice == "2":
        for i, t in enumerate(tasks_list): 
            status = "OK" if t.is_completed else "Wait"
            print(f"{i+1}. {t.description} [{status}]")
    elif choice == "3":
        print("Goodbye!")
        break
        