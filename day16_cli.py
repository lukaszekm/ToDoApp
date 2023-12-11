import time
from functions import get_todos, write_todos


filename = r'todos.txt'
now = time.strftime("%d %b, %Y  %H:%M:%S")

while True:
    print(now)
    user_message = input("Type add, show, edit, delete, clear, complete or exit:")

    todos = get_todos()

    if user_message.startswith("add") or user_message.startswith("new"):
        todo = user_message[4:]
        todos.append(todo + "\n")
        write_todos(todos)

    elif user_message.startswith("show"):
        for index, item in enumerate(todos):
            item = item.title()
            print(f"{index + 1}. {item[:-1]}")
        # new_todos = [item.strip('\n') for item in todos]
    elif user_message.startswith("complete"):
        complete_id = int(user_message[9]) - 1
        todos[complete_id] += " - check"

        write_todos(todos)

    elif user_message.startswith("edit"):
        try:
            edit_id = int(user_message[5]) - 1
            edit = input(f"Editing {str(todos[edit_id])}:")
            todos[edit_id] = edit + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is invalid!")
            continue

    elif user_message.startswith("clear"):
        todos.clear()

    elif user_message.startswith("delete"):
        try:
            delete_id = int(user_message[7]) - 1
            to_delete = todos[delete_id].strip('\n')
            todos.pop(delete_id)
            print(f"{to_delete} removed succesfully!")

            write_todos(todos)

        except IndexError:
            print("Invalid Number!")
            continue

    elif user_message.startswith("exit"):
        print("Bajo!")
        break
    else:
        print("Unknown command!")
