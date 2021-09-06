#Faça um programa que leia nome e média de um aluno, guardando a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
#Maior ou igual a 7 aprovado
#Entre 5 e 7 Recuperação
#Menor que 5 Reprovado

aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
print(30 * '=')
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] >= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'  -{k}: {v}')


