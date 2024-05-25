import functions  # Import the created library of functions
import FreeSimpleGUI as Sg  # Import the third-party library that allows the GUI manipulations

label = Sg.Text("Type in a to-do")

input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")

list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))    # The get_todos returns the todos.txt list that'll be
                                                            # displayed at the GUI
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")

exit_button = Sg.Button("Exit")

window = Sg.Window("My To-do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()   # The read method return a tuple of 2 items, one string that is related to an event
                                    # and a dictionary, that have key and value for all elements of the window

    print(event)  # These print function are to analyse the behavior of the GUI at the terminal
    print(values)

    # Match-case block that analyse the event variable
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"  # Values["to-do"] get the value of dictionary values which key is to-do
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)  # The listbox is updated and now your value is the todos list
        case "Edit":
            selected_todo = values["todos"][0]  # The [0] refers to the selected item on listbox
            new_todo = values["todo"] + "\n"  # The new to-do is what is written at the text box

            todos = functions.get_todos()
            index = todos.index(selected_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WIN_CLOSED:
            break

window.close()
