#Ex.0073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
#na ordem de colocação. Depois mostre:
#A)Apenas os 5 Primeiros colocados.
#B)Os ultimos 4 colocados
#C)Uma lista com os times em ordem alfabéticas
#D)Em que posição na tabela está o time da Chapecoense.'''

times = ('Flamengo', 'Internacional', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico Paranaense',
         'Corinthians', 'Bragantino', 'Ceará', 'Atlético Goianiense',
         'Sport', 'Bahia', 'Fortaleza', 'Vasco', 'Goiás',
         'Coritiba', 'Botafogo', 'Chapecoense')

print(f'Lista de Times do Brasileirão:{times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são:{times[16:20]}')
print(f'Times em Ordem alfabéticas {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")}ª posição')















