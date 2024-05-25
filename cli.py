import functions  # Import created library that contains the functions of the program
import time  # Import standard library from python

# Function from library 'time' that gets the real time and print it
now = time.strftime('%b %d, %Y %H:%M:%S')
print(f'It is {now} ')

while True:
    # Receive the user action without the blank spaces
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # If block to verify if is an add command
    if user_action.startswith("add"):
        # Receive an input from user then append it at the list of todos------------------------------------------------
        # Receive the user quest after the operator add
        todo = user_action[4:] + '\n'  # The [4:] cuts all chars before the fourth char
        todos = functions.get_todos()  # Function to read the todos.txt
        # Append the quest at the list
        todos.append(todo.capitalize())
        functions.write_todos(todos)  # Function to write the updated list at todos.txt
    # If block to verify if is a show command
    elif user_action.startswith("show"):
        # List all the items from todos with an index-------------------------------------------------------------------
        todos = functions.get_todos()
        # Print the list using the enumerate function, that returns an item and your related index
        for index, item in enumerate(todos):
            item = item.strip('\n')  # Removes the break lines from the item
            print(f'{index + 1}- {item}')  # Print the f string and automatically break line
    # If block to verify if is an edit command
    elif user_action.startswith("edit"):
        # Asks for a number input, then a new to-do that will override the number related to-do-------------------------
        # Try-except block to prevent the program to terminate because an error
        try:
            number = int(user_action[5:])
            new_todo = input('Enter a new todo: ') + '\n'
            todos = functions.get_todos()
            todos[number - 1] = new_todo.capitalize()  # Utilize the number - 1 to access the right index of a list
            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid!')
            continue
    # If block to verify if is a complete command
    elif user_action.startswith("complete"):
        # Receive a number and remove the number related to-do from the list--------------------------------------------
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)  # pop method removes an item from the list
            functions.write_todos(todos)
            print(f"Todo '{todo_to_remove}' was removed from the list!")
        except IndexError:
            print('This number is out of the range!')
            continue
    # If block to verify if is an exit command
    elif user_action.startswith("exit"):
        # Break the while loop------------------------------------------------------------------------------------------
        break
    else:
        print('Invalid Answer!')
print("Bye!")
