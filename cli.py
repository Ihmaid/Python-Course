import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'It is {now} ')
while True:
    # Receive the user action
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # Add the quest to the list
    if user_action.startswith("add"):
        # Receive the user quest after the  operator add
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        # Append the quest at the list
        todos.append(todo.capitalize())

        functions.write_todos(todos)
    # Show the list
    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # Print the list using the enumerate function
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}- {item}')
    # Edit a selected quest
    elif user_action.startswith("edit"):
        # Try-except block to prevent the program to terminate because an error
        try:
            number = int(user_action[5:])
            new_todo = input('Enter a new todo: ') + '\n'

            todos = functions.get_todos()

            # Utilize the number - 1 to access the right index of a list
            todos[number - 1] = new_todo.capitalize()

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid!')
            continue
    # Remove a completed quest from the list
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list!")
        except IndexError:
            print('This number is out of the range!')
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print('Invalid Answer!')
print("Bye!")

# TIP: Use the command dir() or help() to understand and discover methods
# TIP: import builtins and use the dir() to look at the functions
