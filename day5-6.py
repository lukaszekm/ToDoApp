filename = r'../txtfiles/todos.txt'
while True:
    user_message = input("Type add, show, edit, delete, clear, complete or exit:")

    with open(filename, 'r') as file:
        todos = file.readlines()

    match user_message.strip():
        case 'add':
            todo = str(input("Enter a to-do: ")) + "\n"
            todos.append(todo)

            with open(filename, 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}. {item[:-1]}")
            # new_todos = [item.strip('\n') for item in todos]
        case 'clear':
            todos.clear()
        case 'delete' | 'erase' | 'remove':
            delete_id = int(input("Which number to delete? ")) - 1
            to_delete = todos[delete_id].strip('\n')
            todos.pop(delete_id)
            print(f"{to_delete} removed succesfully!")
            with open(filename, 'w') as file:
                file.writelines(todos)

        case 'complete':
            complete_id = int(input("Which task to complete? ")) - 1
            todos[complete_id] += " - check"

            with open(filename, 'w') as file:
                file.writelines(todos)

        case 'edit':
            edit_id = int(input("Type number to edit? ")) - 1
            edit = input(f"Editing {str(todos[edit_id])}:")
            todos[edit_id] = edit + '\n'

            with open(filename, 'w') as file:
                file.writelines(todos)

        case 'exit':
            print("Bajo!")
            break
        case _:
            print("Unknown command!")
