import os
"""CLI Calculator to add/subtract/multiply/divide two numbers.
C and AC functions to be added.
a: first calculator entry, b: second entry
op: operation; a = addition, s = subtraction, m = multiplication, d = division
'exit' exits the calculator."""

class Calculator:
    def __init__(self):
        self.isEnd = False
        self.a = 0
        self.b = 0

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a // b

    def allclear(self):
        """Clear everything and start again"""
        os.system('cls')
        self.a, self.b = 0, 0 # set a and b to default values
        self.display() # start calculator again

    def clear(self):
        """Clear the last entry"""
        pass

    def display(self):
        print("""---------\nOperations Guide:\n'+': Addition\n'-': Subtraction\n'*': Multiplication\n'/': Division\n'c': Clear last entry\n'ac': Clear all entries\n'exit': Exit calculator\n---------""")
        result = 0 # if exit is called in the first iteration, result is undefined, causes error
        while not self.isEnd:
            in1 = input('a: ')
            op = input('Operation: ')
            if op == 'exit':
                self.isEnd = True
                break

            elif op == 'ac':
                self.allclear()
                break

            in2 = input('b: ')

            in1 = self.a if in1 == '' else int(in1)
            in2 = self.b if in2 == '' else int(in2)

            if op == '+':
                result = self.add(in1, in2)
                print(result)

            elif op == '-':
                result = self.sub(in1, in2)
                print(result)

            elif op == '*':
                result = self.mul(in1, in2)
                print(result)

            elif op == '/':
                result = self.div(in1, in2)
                print(result)


            else:
                print('Invalid operation.')

            self.a = result
            self.b = in2

calc = Calculator()
calc.display()
