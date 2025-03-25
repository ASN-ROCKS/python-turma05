# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")

# %%
df.tail()

# %%

df.rename(columns={
    "qtdePontos": "qtdPontos",
    "idCliente": "idUsuario"
})

# df.rename(columns={
#     "qtdePontos": "qtdPontos",
#     "idCliente": "idUsuario"
# }, inplace=True)

# %%

df.head(2)

# %%

df.columns = [
    "idCustomer",
    "flEmail",
    "flTwitch",
    "flYouTube",
    "flBlueSky",
    "flInstagram",
    "qtdPoints",
    "dtCreated",
    "dtUpdated",
]

df.head(2)

# %%

df.shape

# %%

df.info()