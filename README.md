# 📈 Projeto de Análise Estatística de Investimentos

Este projeto **automatiza a limpeza**, **segmentação** e **análise estatística** de uma carteira diversificada de investimentos **(Ações, Criptoativos e Renda Fixa)** utilizando **Python e Ciência de Dados.**

## 🚀 Funcionalidades

- **Limpeza e Tratamento de Dados:** Processamento de arquivos CSV brutos, tratamento de tipos (datetime), e cálculo de rendimentos automáticos.
- **Segmentação Automatizada:** Divisão do dataset principal em arquivos individuais por ativo com normalização de nomes.
- **Análise de Risco (Volatilidade):** Cálculo de Variância e Desvio Padrão para medir a estabilidade dos ativos.
- **Estatística Avançada:**
  - **Correlação de Spearman:** Para identificar o grau de sincronia entre ativos, ignorando ruídos (outliers).
  - **Regressão Linear:** Modelagem matemática da relação entre ativos (ex: IPCA vs Selic).
  - **Regressão Logística:** Classificação binária para prever probabilidades de lucro.
- **Métricas de Performance:** Cálculo de R² (Coeficiente de Determinação) e RMSE (Raiz do Erro Quadrático Médio) para validar a precisão das previsões.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Pandas:** Manipulação e limpeza de dados.
- **NumPy:** Cálculos matemáticos vetoriais.
- **SciPy & Scikit-Learn:** Modelagem estatística e Machine Learning.
- **Matplotlib & Seaborn:** Visualização de dados e dashboards.

## 📊 Insights Extraídos

Através da análise, foi possível identificar:
1. O **Bitcoin** apresenta a maior volatilidade da carteira (Desvio Padrão elevado), exigindo aportes menores para gestão de risco.
2. A relação entre **IPCA e Tesouro Selic** demonstra uma correlação positiva, permitindo prever tendências de rendimento.
3. Ativos com **correlação negativa** foram identificados para compor uma estratégia de proteção (hedge).

---
*Projeto desenvolvido como parte dos estudos de Ciência de Dados e Programação.*