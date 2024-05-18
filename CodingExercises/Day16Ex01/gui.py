import FreeSimpleGUI as Sg

label1 = Sg.Text("Enter feet: ")
text_box1 = Sg.InputText(tooltip="Enter the feet")

label2 = Sg.Text("Enter inches: ")
text_box2 = Sg.InputText(tooltip="Enter the inches")

convert_button = Sg.Button("Convert")

window = Sg.Window("Convertor", [[label1, text_box1],
                                 [label2, text_box2],
                                 [convert_button]])

window.read()
window.close()
