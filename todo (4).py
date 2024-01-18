users = {'username': 'password', 'username2': 'password2'}  

tasks = []

def register(username, password):
    if username not in users:
        users[username] = password
        print("User registered successfully!")
    else:
        print("Username already exists! Please choose a different username.")

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials! Please try again!")
        return False

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def edit_task(index, new_task):
    tasks[index] = new_task
    print("Task edited successfully!")

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Task index out of range.")

def list_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def save_tasks(filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print("Tasks saved to file successfully!")

def load_tasks(filename):
    global tasks
    with open(filename, 'r') as file:
        tasks = [line.strip() for line in file]
    print("Tasks loaded from file successfully!")

while True:
    print("\n1. Register\n2. Login\n3. Add Task\n4. Edit Task\n5. Delete Task\n6. List Tasks\n7. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(username, password)
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            print("Logged in as:", username)
    elif choice == '3':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '4':
        index = int(input("Enter index of task to edit: "))
        new_task = input("Enter new task: ")
        edit_task(index - 1, new_task)
    elif choice == '5':
        index = int(input("Enter index of task to delete: "))
        delete_task(index - 1)
    elif choice == '6':
        list_tasks()
    elif choice == '7':
        print("Exit")
        break
    else:
        print("Invalid choice! Please try again.")
