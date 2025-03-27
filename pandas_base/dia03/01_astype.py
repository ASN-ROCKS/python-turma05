# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

# conversão para datetime
clientes["dtAtualizacao"] = pd.to_datetime(clientes["dtAtualizacao"])
clientes

# %%

# conversao para date
clientes["diaAtualizacao"] = clientes["dtAtualizacao"].dt.date

# conversao para string
clientes["diaAtualizacao"] = clientes["diaAtualizacao"].astype(str)

## conversa direta
filtro = clientes["dtAtualizacao"].dt.date.astype(str) == '2025-02-19'

clientes[filtro].shape

# %%

(clientes['qtdePontos'] * 0.5).astype(int)

# %%

(clientes['qtdePontos'] * 0.5).astype(bool).astype(str)

# %%

