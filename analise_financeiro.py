import pandas as pd

# 1. Carregando os dados limpos
df = pd.read_csv('investimentos_intermediario_limpo.csv')

# 2. Criando a coluna de Ganho em Dinheiro (Matemática Financeira)
# Valor do Aporte * (Porcentagem / 100)
df['Ganho_BRL'] = df['Valor_Aporte'] * (df['Rendimento_Mensal_Porcentagem'] / 100)

# 3. Criando o DataFrame de Resumo (Agrupamento por Ativo)
# Aqui pegamos a soma dos aportes e a média dos rendimentos
resumo_ativos = df.groupby('Ativo').agg({
    'Valor_Aporte': 'sum',
    'Rendimento_Mensal_Porcentagem': 'mean',
    'Ganho_BRL': 'sum'
}).rename(columns={
    'Valor_Aporte': 'Total_Investido_BRL',
    'Rendimento_Mensal_Porcentagem': 'Media_Rendimento_Pct',
    'Ganho_BRL': 'Lucro_Total_Estimado'
})

# 4. Calculando a Representatividade (%) de cada ativo na carteira
total_carteira = resumo_ativos['Total_Investido_BRL'].sum()
resumo_ativos['Percentual_da_Carteira'] = (resumo_ativos['Total_Investido_BRL'] / total_carteira) * 100

print("--- RESUMO DA CARTEIRA DE INVESTIMENTOS ---")
print(resumo_ativos)

# Salvando o resultado final
resumo_ativos.to_csv('resumo_final_carteira.csv')