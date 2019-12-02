class Node:
    def __init__(self,v = None, l = None, r = None):
        self.v = v
        self.l = l
        self.r = r

class Tree:
    def __init__(self):
        self.root = Node()
    
    def em_ordem(self, raiz):
        if not raiz:
            return
        self.em_ordem(raiz.l)
        print(raiz.v),
        self.em_ordem(raiz.r)

