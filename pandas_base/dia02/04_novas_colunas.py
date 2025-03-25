# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head(2)

# %%

df["fodase"] = 1
df

# SELECT *,
#        1 as fodase

# FROM clientes

# %%

df["pontos_x10"] = df["qtdePontos"] * 10
df

# %%
df["pontosTwitch"] = df["flTwitch"] * df["qtdePontos"]
df

# %%
df["qtdePontos"].describe()

# %%

import matplotlib.pyplot as plt

df["qtdePontos"].hist(color='#F80373')
plt.title("Histograma de Pontos")
plt.xlabel("Valor Pontos")
plt.ylabel("Frequencia")
plt.show()

# %%

import numpy as np

df["qtdePontosLog"] = np.log(df["qtdePontos"]+1)
df["qtdePontosLog"].hist()
plt.title("Histograma de Log Pontos")
plt.xlabel("Valor Log Pontos")
plt.ylabel("Frequencia")
plt.savefig("log-pontos.png")

# %%

