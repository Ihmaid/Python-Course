import FreeSimpleGUI as Sg
from functions import convert

label1 = Sg.Text("Enter feet: ")
text_box1 = Sg.InputText(tooltip="Enter the feet", key="feet")

label2 = Sg.Text("Enter inches: ")
text_box2 = Sg.InputText(tooltip="Enter the inches", key="inches")

convert_button = Sg.Button("Convert", key="convert")

result = Sg.Text(key="result")

window = Sg.Window("Convertor", [[label1, text_box1],
                                 [label2, text_box2],
                                 [convert_button, result]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "convert":
            feet = values["feet"]
            inches = values["inches"]
            result = f"{round(convert(feet, inches), 3)} m"
            window["result"].update(value=result)
        case Sg.WIN_CLOSED:
            break
window.close()
