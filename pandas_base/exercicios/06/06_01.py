# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

# %%

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv")
# clientes.head()

colunas = ["flTwitch","flYouTube","flBlueSky","flInstagram"]

clientes[colunas].sum(axis=1).describe()

# %%

## 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()

(transacoes.groupby(by=["idCliente"])["idTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(10))

# %%

## 06.03 - Qual usuário teve maior quantidade de pontos debitados?

(transacoes[transacoes["qtdePontos"]<0].groupby(by="idCliente")["qtdePontos"]
                                       .sum()
                                       .sort_values()
                                       .head(1)
                                       )

# %%

# 06.04 - Quem teve mais transações de Streak?

produtos = pd.read_csv("../../data/produtos.csv")
transacoes_produto = pd.read_csv("../../data/transacao_produto.csv")
filtro = transacoes_produto[transacoes_produto["idProduto"]==12]["idTransacao"]

(transacoes[transacoes["idTransacao"].isin(filtro)]
                                    .groupby(by='idCliente')["idTransacao"]
                                    .count()
                                    .sort_values(ascending=False)
                                    .head(1)
                                    )

# %%
# 06.05 - Qual a média de transações / dia?

transacoes["dtCriacao"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes["idTransacao"].nunique() / transacoes["dtCriacao"].nunique()

# %%
# 06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

(transacoes.groupby(by="idCliente")["qtdePontos"]
           .describe())