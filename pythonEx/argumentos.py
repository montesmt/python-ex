#def conta(x, y):
    #return (x+y)/2

#print(conta(10, 5))

#a = conta(10, 15)
#print(a)

def f():
    global x
    print("Recebi", x)
    x += 1
    print("Agora tenho", x)

x = 1
f()
print(x)