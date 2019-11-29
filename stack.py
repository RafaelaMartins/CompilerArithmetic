class Stack:

    def __init__(self):
        self.stack = []
    
    def pop(self):
        self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def leitura(self):
        print(self.stack)
        