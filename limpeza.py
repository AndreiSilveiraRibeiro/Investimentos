import pandas as pd

leitura = pd.read_csv('investimentos_intermediario.csv')

print(leitura)
print(leitura.shape)
leitura.info()

print(leitura['Data'])

print(leitura['Data'])

leitura['Data'] = pd.to_datetime(leitura['Data'], format='mixed', dayfirst=True , errors='coerce')

print(leitura['Data'])    

print(leitura['Investidor'])

leitura['Investidor'] = leitura['Investidor'].str.title()

leitura['Investidor'] = leitura['Investidor'].fillna('Anonimo')

print(leitura['Investidor'])

print(leitura['Ativo'])

leitura['Ativo'] = leitura['Ativo'].str.strip().str.title().replace({"Ações Petr4": "Acoes Petr4"})

print(leitura['Ativo'])

print(leitura['Valor_Aporte'])

mediana = leitura['Valor_Aporte'].median()

leitura['Valor_Aporte'] = leitura['Valor_Aporte'].mask(leitura['Valor_Aporte'] < 0, 0)

leitura['Valor_Aporte'] = leitura['Valor_Aporte'].fillna(mediana)

print(leitura['Valor_Aporte'])

print(leitura['Rendimento_Mensal_Porcentagem'])

print(leitura.isnull().sum())
leitura.dropna(thresh=4, inplace=True)
leitura.drop_duplicates(inplace=True)
print(leitura.isnull().sum())

print(leitura.shape)
leitura.info()

leitura.to_csv('investimentos_intermediario_limpo.csv', index=False)

print("Salvo com sucesso!")

nomes_aivos = leitura['Ativo'].unique()

for ativos in nomes_aivos:

    df_temporario = leitura[leitura['Ativo'] == ativos].copy()

    df_temporario['Analise_rendimento'] = df_temporario['Valor_Aporte'] * (df_temporario['Rendimento_Mensal_Porcentagem'] / 100)

    df_temporario['Analise'] = 'Zero'
    df_temporario.loc[df_temporario['Analise_rendimento'] > 0, 'Analise'] = "Lucro"
    df_temporario.loc[df_temporario['Analise_rendimento'] < 0, 'Analise'] = "Prejuizo"

    nome_arquivo = f"ativo_{ativos.lower().replace(' ', '_')}.csv"

    df_temporario.to_csv(nome_arquivo, index=False)
    print(f"Ativo {ativos} salvo com sucesso!")