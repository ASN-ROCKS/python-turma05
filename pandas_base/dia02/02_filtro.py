# %%

idades = [16,12,15,23,12,17,19,18,23,25,21,20]
#         0  1  2  3  4  5  6  7  8  9  10 11 

check_idade = []
for idade in idades:
    check_idade.append(idade >= 18)

idades_18_mais = []
for i in range(len(idades)):
    if check_idade[i]:
        idades_18_mais.append(idades[i])

idades_18_mais

# %%

import pandas as pd

s_idades = pd.Series(idades)

check_idade_serie = s_idades >= 18
s_idades[check_idade_serie]

# %%

df = pd.read_csv("../data/clientes.csv")
df.head(2)

# %%

filtro = df["qtdePontos"] > 1000

df[filtro]

# %%

colunas_sociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
df[colunas_sociais] == 1

# %%

filtro_email = df["flEmail"] == 1
filtro_twitch = df["flTwitch"] == 1
filtro_geral = filtro_email & filtro_twitch

filtro_geral
# %%
df[filtro_geral].shape