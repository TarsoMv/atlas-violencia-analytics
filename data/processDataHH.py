import pandas as pd

# Carregar os CSVs
p1 = pd.read_csv('data\\homicidios-homens-UF.csv', sep=";", encoding='utf-8')  # Total homens
p2 = pd.read_csv('data\\homicidios-homens-negros-UF.csv', sep=";", encoding='utf-8')  # Homens negros
p3 = pd.read_csv('data\\homicidios-homens-nao-negros-UF.csv', sep=";", encoding='utf-8')  # Homens não negros

# Renomear a coluna "valor" para evitar conflito
p1 = p1.rename(columns={"valor": "ValorHomens"})
p2 = p2.rename(columns={"valor": "ValorHomensNegros"})
p3 = p3.rename(columns={"valor": "ValorHomensNaoNegros"})

# Fazer os joins
df = p1.merge(p2, on=["cod", "nome", "período"], how="outer")
df = df.merge(p3, on=["cod", "nome", "período"], how="outer")

# Ordenar 
df = df.sort_values(by=["cod", "período"])

# Salvar resultado final
df.to_csv('data\\processData\\HomicidiosHomens.csv', index=False, sep=";", encoding='utf-8')

print(df.head())