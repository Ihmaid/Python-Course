import FreeSimpleGUI as Sg
from functions import convert

Sg.theme("Black")

label1 = Sg.Text("Enter feet: ")
text_box1 = Sg.InputText(tooltip="Enter the feet", key="feet")

label2 = Sg.Text("Enter inches: ")
text_box2 = Sg.InputText(tooltip="Enter the inches", key="inches")

convert_button = Sg.Button("Convert", key="convert")
exit_button = Sg.Button("Exit", key="exit")

result = Sg.Text(key="result")

window = Sg.Window("Convertor", [[label1, text_box1],
                                 [label2, text_box2],
                                 [convert_button, exit_button, result]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "convert":
            try:
                feet = values["feet"]
                inches = values["inches"]
                result = f"{round(convert(feet, inches), 3)} m"
                window["result"].update(value=result)
            except:
                Sg.popup("Please provide two numbers.")
        case "exit":
            break
        case Sg.WIN_CLOSED:
            break
window.close()
