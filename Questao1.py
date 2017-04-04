#Escreva uma função recursiva que imprima de um número x até um y

x = int(input("Digite o valor de 'x':"))
y = int(input("Digite o valor de 'y':"))

def imprimir(x,y):
    if(x == y):
        return x
    if(x < y):
        print(x)
        return imprimir(x + 1, y)
    print(x)
    return imprimir(x - 1, y)

print(imprimir(x,y))
