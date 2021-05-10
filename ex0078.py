#Ex.0078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {c}:'))
    lista.append(valor)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição', end='')
for p, v in enumerate(lista):
    if v == max(lista):
        print(f' {p}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} na posição', end='')
for p, v in enumerate(lista):
    if v == min(lista):
        print(f' {p}...', end='')
