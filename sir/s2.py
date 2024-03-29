import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text('Enter your name:'), sg.InputText()],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

# Create the window
window = sg.Window('Simple GUI', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Submit':
        name = values[0]
        sg.popup(f'Hello, {name}!')

# Close the window
window.close()
