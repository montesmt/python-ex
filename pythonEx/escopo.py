def funcao():
    global x
    x = 40
    print('Que variável é essa?', x)

x = 2
funcao()
print(x)