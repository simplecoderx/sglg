import PySimpleGUI as sg

class Calculator:
    def __init__(self):
        self.layout = [
            [sg.Input(size=(15, 1), key='-DISPLAY-', justification='right', readonly=True)],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
            [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')]
        ]
        self.window = sg.Window('Calculator', self.layout)

    def run(self):
        result = ''
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == '=':
                try:
                    result = str(eval(result))
                except:
                    result = 'Error'
            elif event == 'C':
                result = ''
            elif event == 'AC':
                result = ''
            else:
                result += event
            self.window['-DISPLAY-'].update(result)
        self.window.close()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()
