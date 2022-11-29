todos = []


def show_todos():
    for i in todos:
        print(i)


while True:
    action = input("Type add, show, edit or exit: ")
    action = action.strip()
    action = action.lower()

    # match is like Switch in C++
    match action:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo)
        case "show":
            show_todos()
        case "edit":
            num = input("Number of item to edit: ")
            num = int(num)
            try:
                item_edit = input("Type the new item which will replace " + "'" + todos[num] + "'" + ": ")
                todos[num] = item_edit
                show_todos()
            except IndexError:
                print("Invalid number")
        case "exit":
            break
        # the _ is a convention Means something else.
        case _:
            print("Please try again.")
