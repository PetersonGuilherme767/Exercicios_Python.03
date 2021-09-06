#Ex.0085 - Crie programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente.

num = [[], []]
for c in range(1, 8):
    valores = int(input(f'Digite o {c}ª valor:'))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
num[0].sort()
num[1].sort()
print(f'Números Pares digitados:{num[0]}')
print(f'Números Ímpares digitados:{num[1]}')
