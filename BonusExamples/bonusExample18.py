import FreeSimpleGUI as Sg
from zip_extractor import extract_archive

Sg.theme("Black")

label1 = Sg.Text("Select the files to be extracted:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose", key="file")

label2 = Sg.Text("Select the destination folder:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")

output_label = Sg.Text(key="output", text_color="green")

window = Sg.Window("Archive Extractor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["file"]
    folder = values["folder"]
    extract_archive(filepath, folder)
    window["output"].update(value="Extraction Completed")

window.close()
