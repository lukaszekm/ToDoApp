todos = []
i = 1
while True:
    user_message = input("Type \"add\" or \"show\" or \"clear\" or \"exit\":")
    match user_message.strip():
        case 'add':
            todo = str(input("Enter a to-do: "))
            todo = str(f"{i}. {todo}")
            i += 1
            todos.append(todo)

        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                print(item)
        case 'clear':
            todos.clear()
        case 'edit':
            number = int(input("Type number to edit? "))
            edit = input(f"Editing {str(todos[number - 1][3:])}:")

            todos.__setitem__(number - 1, str(f"{number}. ") + edit)
        case 'exit':
            print("Bajo!")
            break
        case _:
            print("Unknown command!")
