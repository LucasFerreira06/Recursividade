#Escreva uma função recursiva que retorna a soma de n até zero

valor = int(input("Digite o valor de 'n':"))

def soma(n):
    if n == 0:
        return n
    return soma(n-1)+n

print(soma(valor))
