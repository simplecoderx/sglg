"""
Dictionary: pair
 age = {'Peter': 5, 'John':7}
for i in age:
    print("Name = %s, Age = %d" %(i, age[i]))
    if age[i] == 5:
        print("true")
        break """


"""
Tuples: values are not modified
 userAge = [21, 5, 24, 25, 99]

for i in userAge:
    if i == 21:
        print("first number is", i) """

class Calculator:
    def __init__(self):
        self.layout = [
            [sg.Input(size=(15, 1), key='-DISPLAY-', justification='right', readonly=True)],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
            [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
        ]
        self.window = sg.Window('Calculator', self.layout)
