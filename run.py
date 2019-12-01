from tree import Node, Tree
from stack import Stack

if __name__ == "__main__":
    test = ["3","2","+","2","*"]
    p = Stack()
    for x in test:
        if x.isdigit():
            new = Node(x,None,None)
            p.push(new)
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
    raiz = Tree()
    raiz.root = p.pop()
    print(raiz.root.v)
    print(raiz.root.r.v)
    print(raiz.root.l.v)
    print(raiz.root.l.r.v)
    print(raiz.root.l.l.v)
    
