import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo")
add_button = Sg.Button("Add")

window = Sg.Window("My To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
