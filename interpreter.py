class Interpreter:
    def __init__(self):
        self.operador=['+','-','/','*']
        self.expression = []
    
    def process(self,root):
        if not root:
            return
        self.process(root.l)
        self.process(root.r)
        if root.v in self.operador:
            if root.v == '+':
                result = self.expression[len(self.expression)-2] + self.expression[len(self.expression)-1]
                del(self.expression[len(self.expression)-2])
                del(self.expression[len(self.expression)-1])
                self.expression.append(result)
            elif root.v == '-':
                result = self.expression[len(self.expression)-2] - self.expression[len(self.expression)-1]
                del(self.expression[len(self.expression)-2])
                del(self.expression[len(self.expression)-1])
                self.expression.append(result)
            elif root.v == '/':
                result = self.expression[len(self.expression)-2] / self.expression[len(self.expression)-1]
                del(self.expression[len(self.expression)-2])
                del(self.expression[len(self.expression)-1])
                self.expression.append(result)
            elif root.v == '*':
                result = self.expression[len(self.expression)-2] * self.expression[len(self.expression)-1]
                del(self.expression[len(self.expression)-2])
                del(self.expression[len(self.expression)-1])
                self.expression.append(result)
            else:
                print('Erro simbolo inválido')
        else:
            self.expression.append(int(root.v))

        

        return self.expression