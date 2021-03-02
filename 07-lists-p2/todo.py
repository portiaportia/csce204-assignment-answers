todos = []
dones = []
print("Welcome to your todo list")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "v":
        listName = input("View (T)odos or (C)ompleted Items? ").lower().strip()
        
        if listName == "t":
            if len(todos) == 0:
                print("You have no todos")
            for todo in todos:
                print(f"- {todo}")
        elif listName == "c":
            if len(dones) == 0:
                print("You have no done items")
            for todo in dones:
                print(f"- {todo}")
        else:
            print("Invalid list name")
    elif command == "a":
        todo = input("Enter todo: ")
        todos.append(todo)
    elif command == "r":
        todo = input("Enter todo: ")

        if todo in todos:
            todos.remove(todo)
            dones.append(todo)
        else:
            print(f"Sorry {todo} is not in your list")
    else:
        print("Invalid command")

print("Goodbye")