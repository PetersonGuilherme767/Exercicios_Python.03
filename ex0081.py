#Ex.0081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A)Quantos números foram digitados.
# B)A lista de valores, ordenada de forma decrescente.
# C)Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um Valor:'))
    lista.append(n)
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Ss':
        continue
    if r in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi digitado')