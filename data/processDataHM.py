import pandas as pd

# Carregar os CSVs
p1 = pd.read_csv('data\\homicidios-mulheres-UF.csv', sep=";", encoding='utf-8')  # Total mulheres
p2 = pd.read_csv('data\\homicidios-mulheres-negras-UF.csv', sep=";", encoding='utf-8')  # Mulheres negras
p3 = pd.read_csv('data\\homicidios-mulheres-nao-negras-UF.csv', sep=";", encoding='utf-8')  # Mulheres não negras

# Renomear a coluna "valor" para evitar conflito
p1 = p1.rename(columns={"valor": "ValorMulheres"})
p2 = p2.rename(columns={"valor": "ValorMulheresNegras"})
p3 = p3.rename(columns={"valor": "ValorMulheresNaoNegras"})

# Fazer os joins
df = p1.merge(p2, on=["cod", "nome", "período"], how="outer")
df = df.merge(p3, on=["cod", "nome", "período"], how="outer")

# Ordenar 
df = df.sort_values(by=["cod", "período"])

# Salvar resultado final
df.to_csv('data\\processData\\HomicidiosMulheres.csv', index=False, sep=";", encoding='utf-8')

print(df.head())