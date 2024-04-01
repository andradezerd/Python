#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Cruzeiro.

classificação2023 = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo',
                'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 
                'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
                'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
                'Santos', 'Goiás', 'Coritiba', 'América-MG')

print (f'\nOs 5 primeiros colocados foram {classificação2023[0:5]}')
print (f'Os 4 rebaixados foram {classificação2023[-4:]}')
print (f'Participantes em ordem alfabética: {sorted(classificação2023)}')
print (f'A posição do Cruzeiro é: {classificação2023.index("Cruzeiro")+1}ª posição')

