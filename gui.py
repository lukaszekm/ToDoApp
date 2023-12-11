import functions
import PySimpleGUI as gui


todo_label = gui.Text("Enter a To-Do: ")
input_box = gui.InputText(tooltip="Enter To-Do")
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")

main_window = gui.Window('To-Do App', layout=[[todo_label], [input_box, add_button], [edit_button]])

main_window.read()
main_window.close()