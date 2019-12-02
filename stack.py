from tree import Node, Tree

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
        print(raiz.root.v)
        print(raiz.root.r.v)
        print(raiz.root.l.v)
        print(raiz.root.l.r.v)
        print(raiz.root.l.l.v)
        print("---------------")
        raiz.em_ordem(raiz.root)
