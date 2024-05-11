FILEPATH = 'todos.txt'


# Function that read the file and return a list with the todos
def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Function that receive as parameter a todos and insert at the file
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
