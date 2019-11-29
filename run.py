from tree import Node, Tree
from stack import Stack

if __name__ == "__main__":
    test = ["3","2","+","2","*"]
    p = Stack()
    for x in test:
        if x.isdigit():
            p.push(x)
            p.leitura()
        else:
            node = Node(x)
            node.r = p.pop()
            node.l = p.pop()
            print(type(node))
            new = node
            print(type(new))
            #raiz.root = Node()
            p.push(new)
            p.leitura()
    raiz = p.stack[0]
    print(raiz.v)
    
