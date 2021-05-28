#Ex.0082 -  crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas litas extras que vão conter apenas os valores pares e os valores impares digitados.
#Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um Valor:'))
    lista.append(n)
    r = str(input('Quer Continuar?[S/N]'))
    if r in 'Ss':
        continue
    if r in 'Nn':
        break
print(f'A lista completa é {lista}')
for p, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores Pares são {pares}')
print(f'Os valores Impares são {impares}')

