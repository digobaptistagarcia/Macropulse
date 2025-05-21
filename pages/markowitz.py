# import streamlit as st
# st.header("Markowitz")
# st.write("Get in touch with us for inquiries and support.")
# st.markdown("""titulo:
            

#             explicação



#             conclusao

# """)

# import numpy as np  # Importa a biblioteca NumPy
# import matplotlib.pyplot as plt  # Importa a biblioteca para plotar gráficos
# import pandas as pd

# # Define os retornos esperados para 3 ativos
# retornos_esperados = np.array([0.12, 0.18, 0.14])

# # Define a matriz de covariância entre os ativos
# covariancia = np.array([[0.1, 0.03, 0.05],
#                         [0.03, 0.12, 0.07],
#                         [0.05, 0.07, 0.15]])

# # Taxa livre de risco
# rf = 0.05


# # Gera portfólios aleatórios
# def gerar_portfolios(n=1000):
#     pesos = np.random.rand(n, 3)  # Gera pesos aleatórios
#     pesos = pesos / pesos.sum(axis=1, keepdims=True)  # Normaliza para somar 1
#     retornos = np.dot(pesos, retornos_esperados)  # Calcula retorno de cada portfólio
#     riscos = np.sqrt(np.einsum('ij,jk,ik->i', pesos, covariancia, pesos))  # Calcula risco
#     sharpe_ratios = (retornos - rf) / riscos  # Calcula Sharpe Ratio considerando rf
#     return pesos, retornos, riscos, sharpe_ratios

# # Calcula o portfólio de mínima variância

# def port_min_variancia():
#     inv_cov = np.linalg.inv(covariancia)  # Inverso da matriz de covariância
#     um = np.ones(len(retornos_esperados))
#     w_min_var = inv_cov @ um / (um @ inv_cov @ um)  # Pesos do portfólio de menor risco
#     retorno_min_var = np.dot(w_min_var, retornos_esperados)  # Retorno do portfólio mínimo risco
#     risco_min_var = np.sqrt(np.dot(w_min_var, np.dot(covariancia, w_min_var)))  # Risco mínimo
#     risk_contribution = w_min_var * np.dot(covariancia, w_min_var) / risco_min_var  # Contribuição do risco
#     return w_min_var, retorno_min_var, risco_min_var, risk_contribution

# # Calcula o portfólio que maximiza o Sharpe Ratio
# def port_max_sharpe(retornos, riscos, pesos):
#     idx_max_sharpe = np.argmax((retornos - rf) / riscos)  # Encontra o índice do maior Sharpe Ratio
#     w_max_sharpe = pesos[idx_max_sharpe]
#     risco_max_sharpe = riscos[idx_max_sharpe]
#     retorno_max_sharpe = retornos[idx_max_sharpe]
#     risk_contribution = w_max_sharpe * np.dot(covariancia, w_max_sharpe) / risco_max_sharpe  # Contribuição do risco
#     return w_max_sharpe, retorno_max_sharpe, risco_max_sharpe, risk_contribution

# # Gera os portfólios
# pesos, retornos, riscos, sharpe_ratios = gerar_portfolios()
# w_min_var, retorno_min_var, risco_min_var, risk_contrib_min_var = port_min_variancia()
# w_max_sharpe, retorno_max_sharpe, risco_max_sharpe, risk_contrib_max_sharpe = port_max_sharpe(retornos, riscos, pesos)

# # Criação do DataFrame com informações das carteiras
# ativos = ['Ativo 1', 'Ativo 2', 'Ativo 3']

# portfolio_df = pd.DataFrame({
#     'Ativos': ativos * 2,
#     'Carteira': ['Min Variance'] * 3 + ['Max Sharpe'] * 3,
#     'Peso': np.concatenate([w_min_var, w_max_sharpe]),
#     'Retorno Esperado': np.concatenate([w_min_var * retorno_min_var, w_max_sharpe * retorno_max_sharpe]),
#     'Risco Contribuição': np.concatenate([risk_contrib_min_var, risk_contrib_max_sharpe])
# })

# print(portfolio_df)

# # Calcula a Linha de Alocação de Capital (LAC)
# x_risco = np.linspace(0, max(riscos) * 1.2, 100)
# y_retorno = rf + ((retorno_max_sharpe - rf) / risco_max_sharpe) * x_risco

# # Calcula o portfólio ótimo combinando renda fixa e variável
# peso_rf = 0.3  # 30% em renda fixa
# peso_var = 1 - peso_rf  # 70% no portfólio de máximo Sharpe
# risco_otimo = peso_var * risco_max_sharpe
# retorno_otimo = peso_rf * rf + peso_var * retorno_max_sharpe

# # Plota os portfólios e destaca o de menor risco e o de maior Sharpe Ratio
# plt.figure(figsize=(8, 5))
# plt.scatter(riscos, retornos, c=sharpe_ratios, cmap='viridis', marker='o', alpha=0.5)
# plt.colorbar(label='Sharpe Ratio')
# plt.scatter(risco_min_var, retorno_min_var, color='red', marker='*', s=200, label='Min Var Portfolio')
# plt.scatter(risco_max_sharpe, retorno_max_sharpe, color='blue', marker='*', s=200, label='Max Sharpe Portfolio')
# plt.scatter(risco_otimo, retorno_otimo, color='green', marker='*', s=200, label='Optimal Portfolio')
# plt.plot(x_risco, y_retorno, color='black', linestyle='--', label='Capital Market Line (LAC)')
# plt.xlabel('Risco (Desvio Padrão)')
# plt.ylabel('Retorno Esperado')
# plt.title('Fronteira Eficiente de Markowitz e LAC')
# plt.legend()
# plt.show()


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.image("./imagens/fundo_de_tela5.png")
st.markdown("""
### Markowitz Theory

Modern Portfolio Theory (MPT), or Markowitz Theory, is an investment theory that aims to maximize expected return for a given level of risk, or minimize risk for a given level of expected return. It is based on the idea of diversification, that is, investing in a variety of different assets to reduce the overall risk of the portfolio.

### Explanation

The Markowitz model uses the mean and variance of asset returns to construct the efficient frontier, which represents the set of portfolios that offer the highest expected return for each level of risk. The investor can choose the portfolio that best suits their risk profile, that is, their tolerance for loss.

### Conclusion

Markowitz Theory is a powerful tool for investment portfolio management. It allows investors to build diversified and efficient portfolios that maximize expected return for a given level of risk. However, it is important to remember that the Markowitz model is based on some simplified assumptions, such as the normality of asset returns and the rationality of investors.

""")

# Define expected returns for 3 assets
expected_returns = np.array([0.12, 0.18, 0.14])

# Define the covariance matrix between assets
covariance = np.array([[0.1, 0.03, 0.05],
                       [0.03, 0.12, 0.07],
                       [0.05, 0.07, 0.15]])

# Risk-free rate
rf = 0.05

# Generate random portfolios
def generate_portfolios(n=1000):
    weights = np.random.rand(n, 3)
    weights = weights / weights.sum(axis=1, keepdims=True)
    returns = np.dot(weights, expected_returns)
    risks = np.sqrt(np.einsum('ij,jk,ik->i', weights, covariance, weights))
    sharpe_ratios = (returns - rf) / risks
    return weights, returns, risks, sharpe_ratios

# Calculate the minimum variance portfolio
def min_variance_portfolio():
    inv_cov = np.linalg.inv(covariance)
    ones = np.ones(len(expected_returns))
    w_min_var = inv_cov @ ones / (ones @ inv_cov @ ones)
    min_var_return = np.dot(w_min_var, expected_returns)
    min_var_risk = np.sqrt(np.dot(w_min_var, np.dot(covariance, w_min_var)))
    risk_contribution = w_min_var * np.dot(covariance, w_min_var) / min_var_risk
    return w_min_var, min_var_return, min_var_risk, risk_contribution

# Calculate the portfolio that maximizes the Sharpe Ratio
def max_sharpe_portfolio(returns, risks, weights):
    idx_max_sharpe = np.argmax((returns - rf) / risks)
    w_max_sharpe = weights[idx_max_sharpe]
    max_sharpe_risk = risks[idx_max_sharpe]
    max_sharpe_return = returns[idx_max_sharpe]
    risk_contribution = w_max_sharpe * np.dot(covariance, w_max_sharpe) / max_sharpe_risk
    return w_max_sharpe, max_sharpe_return, max_sharpe_risk, risk_contribution

# Generate portfolios
weights, returns, risks, sharpe_ratios = generate_portfolios()
w_min_var, min_var_return, min_var_risk, risk_contrib_min_var = min_variance_portfolio()
w_max_sharpe, max_sharpe_return, max_sharpe_risk, risk_contrib_max_sharpe = max_sharpe_portfolio(returns, risks, weights)

# Create DataFrame with portfolio information
assets = ['Asset 1', 'Asset 2', 'Asset 3']

portfolio_df = pd.DataFrame({
    'Assets': assets * 2,
    'Portfolio': ['Min Variance'] * 3 + ['Max Sharpe'] * 3,
    'Weight': np.concatenate([w_min_var, w_max_sharpe]),
    'Expected Return': np.concatenate([w_min_var * min_var_return, w_max_sharpe * max_sharpe_return]),
    'Risk Contribution': np.concatenate([risk_contrib_min_var, risk_contrib_max_sharpe])
})

st.write(portfolio_df)

# Calculate the Capital Allocation Line (CAL)
x_risk = np.linspace(0, max(risks) * 1.2, 100)
y_return = rf + ((max_sharpe_return - rf) / max_sharpe_risk) * x_risk

# Calculate the optimal portfolio combining risk-free and risky assets
risk_free_weight = 0.3
risky_weight = 1 - risk_free_weight
optimal_risk = risky_weight * max_sharpe_risk
optimal_return = risk_free_weight * rf + risky_weight * max_sharpe_return

# Plot portfolios and highlight the minimum risk and maximum Sharpe Ratio portfolios
fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(risks, returns, c=sharpe_ratios, cmap='viridis', marker='o', alpha=0.5)
plt.colorbar(scatter, label='Sharpe Ratio')
ax.scatter(min_var_risk, min_var_return, color='red', marker='*', s=200, label='Min Var Portfolio')
ax.scatter(max_sharpe_risk, max_sharpe_return, color='blue', marker='*', s=200, label='Max Sharpe Portfolio')
ax.scatter(optimal_risk, optimal_return, color='green', marker='*', s=200, label='Optimal Portfolio')
ax.plot(x_risk, y_return, color='black', linestyle='--', label='Capital Market Line (CAL)')
ax.set_xlabel('Risk (Standard Deviation)')
ax.set_ylabel('Expected Return')
ax.set_title('Markowitz Efficient Frontier and CAL')
ax.legend()
st.pyplot(fig)


# ... (rest of the code: data, functions, calculations, plotting) ...

# Explanation Section
st.markdown("""
## Understanding Key Concepts

### Markowitz Theory

**What it is:** Modern Portfolio Theory (MPT), developed by Harry Markowitz, is a framework for constructing portfolios that maximize expected return for a given level of risk. It emphasizes diversification to reduce risk.

**Why it's important:** It provides a systematic approach to portfolio construction, moving beyond simply chasing high returns and considering the relationship between risk and return.

### Minimum Variance Portfolio

**What it is:** The portfolio with the lowest possible risk (variance) among all possible portfolios of the given assets.

**Why it's important:** It serves as the base of the efficient frontier and is crucial for risk-averse investors who prioritize minimizing risk.

### Maximum Sharpe Ratio Portfolio

**What it is:** The portfolio that offers the highest Sharpe Ratio, which measures risk-adjusted return (excess return per unit of risk).

**Why it's important:** It represents the optimal portfolio for investors who want to maximize return per unit of risk taken.

### Capital Market Line (CML) / Capital Allocation Line (CAL)

**What it is:** A line that represents the risk-return trade-off available to investors when they combine a risk-free asset with the market portfolio (or in this case, the maximum Sharpe ratio portfolio).

**Why it's important:** It shows how investors can leverage a risk-free asset to achieve different risk-return profiles beyond the efficient frontier. It also provides a visual representation of how to combine the risk-free asset and the risky portfolio.

### Optimal Portfolio

**What it is:** The portfolio that best aligns with an investor's risk tolerance and return objectives. It's often a combination of the risk-free asset and the maximum Sharpe ratio portfolio, determined by the investor's desired risk level.

**Why it's important:** It provides a personalized investment strategy that reflects the investor's individual needs and preferences.
""")

# ... (rest of the code: plotting and displaying results) ...