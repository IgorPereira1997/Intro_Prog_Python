# -*- coding: utf-8 -*-
times = {"SP": ['Corithians', 'São Paulo', 'Palmeiras', 'Santos', 'Bragantino'],
         "RJ": ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo'],
         "RS": ['Internacional', 'Grêmio'],
         "PR": ['Coritba', 'Athletico'],
         "CE": ['Fortaleza', 'Ceará'],
         "MG": 'Atlético-MG',
         "PE": 'Sport',
         "BA": 'Bahia',
         "GO": ['Atlético-GO', 'Goiás'] }

print(times["SP"])

for chave in times:
    print(chave, ":", times[chave])

for i in times.items():
    print(i)
for i in times.values():
    print(i)

for i in times.keys():
    print(i)