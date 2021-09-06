#Crie um programa que leia, nome, ano de nascimento, e carteira de trabalho e cadastre-os
#com idade em um dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente além da idade, com quantos anos a pessoa
#vai se aposentar.

from datetime import datetime
dados = {}
dados['Nome:'] = str(input('Nome:'))
idade = int(input('Ano de Nascimento:'))
dados['Idade atual:'] = datetime.now().year - idade
dados['Carteira:'] = int(input('Carteira de Trabalho (se não tem digite 0):'))
if dados['Carteira:'] != 0:
    dados['Ano contratação:'] = int(input('Ano de contratação:'))
    dados['salário'] = float(input('Salário R$:'))
    dados['Aposentadoria'] = dados['Idade atual:'] + ((dados['Ano contratação:'] + 35) - datetime.now().year)
print(60 * '=')
for k, v in dados.items():
    print(f'  - {k} {v}')


