import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats

leitura = pd.read_csv('investimentos_intermediario_limpo.csv')
petr4 = pd.read_csv("ativo_acoes_petr4.csv")
vale3 = pd.read_csv("ativo_ações_vale3.csv")
bitcoin = pd.read_csv("ativo_bitcoin.csv")
cripto = pd.read_csv("ativo_cripto.csv")
ipca = pd.read_csv("ativo_ipca+.csv")
tesouro_selic = pd.read_csv("ativo_tesouro_selic.csv")

print(f"DataFrame principal: \n{leitura}")
print(f"Ativo petr4: \n{petr4}")
print(f"Ativo vale3: \n{vale3}")
print(f"Ativo bitcon: \n{bitcoin}")
print(f"Ativo cripto: \n{cripto}")
print(f"Ativo ipca: \n{ipca}")
print(f"Ativo tesouro selic: \n{tesouro_selic}")

# --- PETR4 ---
variancia_petr = petr4['Rendimento_Mensal_Porcentagem'].var()
desvio_petr = petr4['Rendimento_Mensal_Porcentagem'].std()

# --- Vale3 ---
variancia_vale = vale3['Rendimento_Mensal_Porcentagem'].var()
desvio_vale = vale3['Rendimento_Mensal_Porcentagem'].std()

# --- BITCOIN ---
variancia_btc = bitcoin['Rendimento_Mensal_Porcentagem'].var()
desvio_btc = bitcoin['Rendimento_Mensal_Porcentagem'].std()

# --- Cripto ---
variancia_cripto = cripto['Rendimento_Mensal_Porcentagem'].var()
desvio_cripto = cripto['Rendimento_Mensal_Porcentagem'].std()

# --- IPCA ---
variancia_ipca = ipca['Rendimento_Mensal_Porcentagem'].var()
desvio_ipca = ipca['Rendimento_Mensal_Porcentagem'].std()

# --- Tesouro Selic ---
variancia_tesouro = tesouro_selic['Rendimento_Mensal_Porcentagem'].var()
desvio_tesouro = tesouro_selic['Rendimento_Mensal_Porcentagem'].std()

print(f"PETR4   - Variância: {variancia_petr:.2f} | Desvio Padrão: {desvio_petr:.2f}%")
print(f"Vale3   - Variância: {variancia_vale:.2f} | Desvio Padrão: {desvio_vale:.2f}%")
print(f"Bitcoin - Variância: {variancia_btc:.2f} | Desvio Padrão: {desvio_btc:.2f}%")
print(f"Cripto   - Variância: {variancia_cripto:.2f} | Desvio Padrão: {desvio_cripto:.2f}%")
print(f"IPCA - Variância: {variancia_ipca:.2f} | Desvio Padrão: {desvio_ipca:.2f}%")
print(f"Tesouro Selic - Variância: {variancia_tesouro:.2f} | Desvio Padrão: {desvio_tesouro:.2f}%")

# Criamos um DataFrame só com os rendimentos de cada ativo
# (Para isso, os DataFrames precisam ter o mesmo tamanho ou usar a data como índice)

comparativo = pd.DataFrame({
    
    'PETR4': petr4['Rendimento_Mensal_Porcentagem'],
    'Vale3': vale3['Rendimento_Mensal_Porcentagem'],
    'Bitcoin': bitcoin['Rendimento_Mensal_Porcentagem'],
    'Cripto': cripto['Rendimento_Mensal_Porcentagem'],
    'IPCA': ipca['Rendimento_Mensal_Porcentagem'],
    'Tesouro Selic': tesouro_selic['Rendimento_Mensal_Porcentagem']

})

# Calculando Spearman
matriz_correlacao = comparativo.corr(method='spearman')

print("Matriz de Correlação de Spearman:")
print(matriz_correlacao)

# 1. Alinhando os dados para evitar o erro de 'shapes incompatible'
comparativo_limpo = comparativo.dropna()

x = comparativo_limpo['IPCA']
y = comparativo_limpo['Tesouro Selic']

# 2. O cálculo da Regressão
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# 3. Agora os prints para a gente ver o resultado!
print("-" * 30)
print("RESULTADOS DA REGRESSÃO LINEAR")
print("-" * 30)
print(f"Equação: Rendimento_Selic = ({slope:.4f} * Valor_IPCA) + ({intercept:.4f})")
print(f"Coeficiente de Determinação (R²): {r_value**2:.4f}")
print(f"P-Value: {p_value:.4f}")
print("-" * 30)

if p_value < 0.05:
    print("Conclusão: Existe uma relação estatisticamente relevante entre esses ativos!")
else:
    print("Conclusão: A relação entre esses ativos é fraca ou fruto do acaso.")


# Cálculo do RMSE (Root Mean Squared Error)
previsoes = (slope * x) + intercept
erros = y - previsoes
rmse = np.sqrt(np.mean(erros**2))

print(f"RMSE: {rmse:.4f}")
print(f"Isso significa que sua previsão erra, em média, {rmse:.2f}% para mais ou para menos.")

# 1. Criamos a categoria: 1 para Lucro, 0 para Prejuízo
comparativo_limpo['Status_Petr4'] = (comparativo_limpo['PETR4'] > 0).astype(int)

# 2. Preparamos os dados (o Sklearn exige que o X seja uma matriz)
X_log = comparativo_limpo[['Tesouro Selic']] 
y_log = comparativo_limpo['Status_Petr4']

# 3. Treinamos o modelo
modelo_log = LogisticRegression()
modelo_log.fit(X_log, y_log)

# 4. Verificamos a chance de lucro se a Selic render 1%
probabilidade = modelo_log.predict_proba([[1.0]])[0][1]
print(f"Chance de lucro na PETR4 com Selic a 1%: {probabilidade*100:.2f}%")