import pandas as pd

p1 = pd.read_csv('data\\homicidios-UF.csv', sep=";", encoding='utf-8')
p2 = pd.read_csv('data\\populacao-UF.csv', sep=",", encoding='utf-8')

p1.columns = p1.columns.str.strip()
p2.columns = p2.columns.str.strip()


df = p1.merge(p2, on=['nome', 'período'], how='outer')

df = df.sort_values(by=["nome", "período"])

df.to_csv('data\\processData\\Habitantes-Homicidios-UF.csv', index=False, sep=";", encoding='utf-8')