""" class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print("Hello")

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")


parent = ParentClass()
child = ChildClass( )
 """
import textwrap
import PySimpleGUI as sg

class FASForm:
    def __init__(self):
        self.layout = self.create_layout()
        """ self.window = sg.Window('FAS Form', self.layout) """

    def create_layout(self):
        print("create layout")

child = FASForm()