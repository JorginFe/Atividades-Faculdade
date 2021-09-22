#Faça um código que retorne o reverso dos números inseridos
n=int(input("Digite um número inteiro: "))
def reverso(x):
 x=str(x)
 return x[::-1]
print("O reverso de %d é: "%n,reverso(n))