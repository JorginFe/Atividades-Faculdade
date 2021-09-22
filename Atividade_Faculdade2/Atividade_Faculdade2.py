#Faça um programa com uma fução que informe se existe algum valor repetido ou se deseja adicionar elementos.

números = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in números:
        números.append(n)
        print('O valor foi inserido em sua lista')
    else:
        print('O valor já existe na lista, portanto não será adicionado')
    r = str(input('Deseja conitnuar? [sim/não]'))
    if r in 'Nãonão':
         break
print('='*50)
print(f'Números da sua lista: {números}')
