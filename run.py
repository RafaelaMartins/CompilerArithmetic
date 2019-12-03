from stack import Stack

if __name__ == "__main__":
    files = []
    inputs = []
    files = open('input.txt', 'r')
    linha = files.read()
    for x in linha:
        if x != ' ':
            inputs.append(x)
    print(inputs)
    p = Stack(inputs)
    files.close()

    #test = ["10","2","/","30","20","-","5","*","+"]
    #test = ["8","2","/","9","4","-","5","*","+"]
    #p = Stack(files)
    
    
