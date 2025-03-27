# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

def plus_100_t_yt(row):
    if row["flTwitch"] == 1 and row["flYouTube"] == 1:
        return row["qtdePontos"] + 100
    else:
        return row["qtdePontos"]
    
df.apply(plus_100_t_yt, axis=1)
df["flTwitch"] * df["flYouTube"] * 100 + df["qtdePontos"]

# %%

df.apply(lambda row: "engajado" if row["flTwitch"] == 1 and row["flYouTube"] == 1 else "nao engajado", axis=1)

# %%

numero = 100
# valor = ""
# if numero > 100:
#     valor = "muito"
# else:
#     valor = "baixo"

valor = "muito" if numero > 100 else "baixo"
valor