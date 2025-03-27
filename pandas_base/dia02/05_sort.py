# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%

clientes.sort_values(by="qtdePontos").tail(5)

# %%

clientes.sort_values(by="qtdePontos", ascending=False).head(5)

# %%

df = pd.DataFrame({
    "nome": ["teo", "nah", "mah", "lara",],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo",],
    "idade": [32, 35, 4, 32],
})

df.sort_values(by=["idade", "nome"], ascending=[False, True])