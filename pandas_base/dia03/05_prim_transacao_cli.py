# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

(df.sort_values(["dtCriacao"])
   .drop_duplicates(subset=["idCliente"], keep='first'))

# %%

(df.sort_values(["dtCriacao"])
   .drop_duplicates(subset=["idCliente"], keep='first'))

# %%

# 05.05 - Selecione a primeira transação diária de cada cliente.

df["diaCriacao"] = pd.to_datetime(df["dtCriacao"]).dt.date
(df.sort_values("dtCriacao")
   .drop_duplicates(subset=["idCliente", "diaCriacao"]))