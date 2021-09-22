#Faça um programa que retorne a soma de três números

def soma(a, b, c):
    res = a + b + c
    return res

a = int(input("Valor de A:"))
b = int(input("Valor de B:"))
c = int(input("Valor de C:"))

print("Soma =", soma(a, b, c))