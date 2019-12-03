from tree import Node, Tree
from interpreter import Interpreter

class Stack:

    def __init__(self,test):
        self.stack = []
        self.run(test)
    
    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def leitura(self):
        print(self.stack)
    
    def run(self, test):
        for x in test:
            if x.isdigit():
                new = Node(x,None,None)
                self.push(new)
                self.leitura()
            else:
                node = Node(x)
                node.r = self.pop()
                node.l = self.pop()
                new = node
                self.push(new)
        raiz = Tree()
        raiz.root = self.pop()
        
        print("---------------")
        raiz.em_ordem(raiz.root)
        result = Interpreter()
        x = result.process(raiz.root)
        print(x)
        output = open('saida.txt', 'w')
        output.write(str(x))
        output.close()
