#Ex.0084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com pessoas mais leves.

principal = []
temporario = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome:')))
    temporario.append(float(input('Peso Kg:')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Deseja continuar?'))
    if resposta in 'Nn':
        break
print(f'Ao todo você cadastrou {len(principal)} pessoas')
print(f'O maior peso cadastrado é {maior}Kg de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso cadastrado é {menor}Kg de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

#############################################################################
lista = []
peso = []
pessoas = []
while True:
    lista.append(str(input('Nome:')))
    lista.append(float(input('Peso:')))
    pessoas.append(lista[:])
    peso.append(lista[1])
    lista.clear()
    r = str(input('Quer continuar?'))
    if r in 'Nn':
        break
print(f'Ao todo foram {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi {max(peso)}', end='')
for p in pessoas:
    if p[1] == max(peso):
        print(f' [{p[0]}]')
