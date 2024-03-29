class SomeClass:
    def __init__(self):
        print('This is SomeClass')
    def someMethod(self, a, b):
        print('The value of a is', a)
        b = 5
        print('The value of b is', b)

class SomeOtherClass:
    def someMethod(self,c):
        self.c = 5