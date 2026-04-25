import pandas as pd
import numpy as np
from scipy import stats

leitura = pd.read_csv('investimentos_intermediario_limpo.csv')

print(leitura.describe())
print(leitura)

leitura['z_score_aporte'] = np.abs(stats.zscore(leitura['Valor_Aporte']))
leitura['z_score_rendimento'] = np.abs(stats.zscore(leitura['Rendimento_Mensal_Porcentagem']))

limite = 3

print(len(leitura[leitura['z_score_aporte'] > limite]))
print(len(leitura[leitura['z_score_rendimento'] > limite]))

anomalias_rendimento = leitura[leitura['z_score_rendimento'] > limite]

anomalias_rendimento.to_csv('outliers_rendimento.csv', index=False)

print('Salvo com sucesso!')