import PySimpleGUI as sg

layout = [[sg.Text('Enter your name:'), sg.InputText()], [sg.Button('OK')]]

window = sg.Window('Desktop Application', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'OK':
        print(f'Hello, {values[0]}!')
        break

window.close()

# Output:
# 'Hello, [Your Name]!' is printed to the console when the 'OK' button is clicked
