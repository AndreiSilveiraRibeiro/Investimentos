import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CARREGAR OS DADOS (O que faltava para o erro sumir)
petr4 = pd.read_csv("ativo_acoes_petr4.csv")
vale3 = pd.read_csv("ativo_ações_vale3.csv")
bitcoin = pd.read_csv("ativo_bitcoin.csv")
cripto = pd.read_csv("ativo_cripto.csv")
ipca = pd.read_csv("ativo_ipca+.csv")
tesouro_selic = pd.read_csv("ativo_tesouro_selic.csv")

# 2. CRIAR O COMPARATIVO (Alinhando os dados para os gráficos)
comparativo = pd.DataFrame({
    'PETR4': petr4['Rendimento_Mensal_Porcentagem'],
    'Vale3': vale3['Rendimento_Mensal_Porcentagem'],
    'Bitcoin': bitcoin['Rendimento_Mensal_Porcentagem'],
    'Cripto': cripto['Rendimento_Mensal_Porcentagem'],
    'IPCA': ipca['Rendimento_Mensal_Porcentagem'],
    'Tesouro Selic': tesouro_selic['Rendimento_Mensal_Porcentagem']
})

comparativo_limpo = comparativo.dropna()
matriz_correlacao = comparativo_limpo.corr(method='spearman')

# 3. CONFIGURAÇÃO DOS GRÁFICOS
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (15, 10)

# Criando a figura com subplots
fig, axes = plt.subplots(2, 2)

# --- GRÁFICO 1: Histórico de Volatilidade ---
axes[0, 0].plot(bitcoin['Rendimento_Mensal_Porcentagem'], label='Bitcoin', color='orange', alpha=0.7)
axes[0, 0].plot(petr4['Rendimento_Mensal_Porcentagem'], label='PETR4', color='blue', alpha=0.7)
axes[0, 0].set_title('Volatilidade: BTC vs PETR4 (Desvio Padrão)')
axes[0, 0].legend()

# --- GRÁFICO 2: Regressão Linear (IPCA vs Selic) ---
sns.regplot(ax=axes[0, 1], data=comparativo_limpo, x='IPCA', y='Tesouro Selic', 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[0, 1].set_title('Regressão Linear: Influência do IPCA na Selic')

# --- GRÁFICO 3: Ranking de Risco ---
ativos_std = comparativo_limpo.std().sort_values(ascending=False)
sns.barplot(ax=axes[1, 0], x=ativos_std.index, y=ativos_std.values, palette='viridis')
axes[1, 0].set_title('Risco por Ativo (Desvio Padrão %)')

# --- GRÁFICO 4: Mapa de Calor (Correlação) ---
sns.heatmap(matriz_correlacao, ax=axes[1, 1], annot=True, cmap='coolwarm', fmt=".2f")
axes[1, 1].set_title('Matriz de Correlação (Estratégia de Diversificação)')

plt.tight_layout()
plt.show()