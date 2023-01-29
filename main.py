while True:
    action = input("Type add, show, edit, done or exit: ")
    action = action.strip()
    action = action.lower()

    # match is like Switch in C++
    match action:
        case "add":
            todo = input("Enter todo: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            def show_todos():
                for index, i in enumerate(todos):
                    print(f"{index + 1}.{i}")
        case "edit":
            num = input("Number of item to edit: ")
            """-1 is to compensate for the plus 1 in the for loop, the enumeration will start at 1 
            instead of 0"""
            num = int(num) - 1
            try:
                item_edit = input("Type the new item which will replace " + "'" + todos[num] + "'" + ": ")
                todos[num] = item_edit
                show_todos()
            except IndexError:
                print("Invalid number")
        case "done":
            complete = input("Enter the number of the item completed: ")
            complete = int(complete)
            todos.pop(complete - 1)
        case "exit":
            break
        # the _ is a convention Means something else.
        case _:
            print("Please try again.")
