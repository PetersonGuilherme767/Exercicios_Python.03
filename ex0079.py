#Ex.0079 - Crie um programa onde o usuário possa digitar vários valores numérico e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
#digitados em ordem crescente.

números = []

while True:
    n = int(input('Digite um valor:'))
    if n not in números:
        números.append(n)
    else:
        print('Valor duplicado! Digite outro valor...')
    r = str(input('Deseja continuar [S/N]?'))
    if r in 'Ss':
        continue
    if r in 'Nn':
        break
    else:
        print('Opção inválida!')
números.sort()
print(f'Você digitou {números}')

