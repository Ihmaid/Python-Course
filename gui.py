import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")

window = Sg.Window("My To-do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            selected_todo = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(selected_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WIN_CLOSED:
            break

window.close()
