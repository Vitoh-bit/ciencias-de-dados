
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados de vendas da sua tabela
dados = [120, 150, 160, 170, 190, 200, 210, 215, 220, 240, 250, 260]

# Calcular quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2 (mediana)={quartis[1]}, Q3={quartis[2]}')

plt.boxplot(dados, vert=False)
plt.title('Boxplot das Vendas Mensais')
plt.xlabel('Vendas')
plt.show()
plt.savefig('vendasboxplot.png')