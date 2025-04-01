# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

df[df["qtdePontos"]>0]["qtdePontos"] .sum()

# %%

df["qtdePontos"].describe()

# %%

df.describe()

# %%
df.columns

# %%

df_transacao_produto = pd.read_csv("../data/transacao_produto.csv")
df_transacao_produto["idProduto"] = df_transacao_produto["idProduto"].astype(str)
df_transacao_produto.describe()

# %%
df_transacao_produto[['idTransacaoProduto','idTransacao','idProduto']].describe()

# %%

df.groupby(by="idCliente")[["qtdePontos"]].sum()

# %%

df = pd.DataFrame(
    {
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "sobrenome_pai": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "idade": [32, 35, 32, 30, 30, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

def amplitude(x):
    return max(x) - min(x)

grouped = df.groupby(by="sobrenome").agg({"idade": "mean",
                                           "salario": ["median", "mean", amplitude],
                                           "nome":"count"})

# %%
grouped[[("salario", "mean"), ("salario", "amplitude")]]

# %%

grouped.columns = ["idade_media",
                   "salario_mediano",
                   "salario_medio",
                   "salario_amplitude",
                   "nome_qde"]
grouped