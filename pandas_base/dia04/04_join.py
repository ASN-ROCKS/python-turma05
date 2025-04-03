# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacao_produto = pd.read_csv("../data/transacao_produto.csv")
produtos = pd.read_csv("../data/produtos.csv")

# %%

join = (transacoes.merge(right=transacao_produto,
                        how="left",
                        #  on=["idTransacao"]
                        right_on=["idTransacao"],
                        left_on=["idTransacao"])
                   .merge(produtos) )


filtro = join["descProduto"].str.contains("Streak")

(join[filtro].groupby("idCliente")["idTransacao"]
             .count()
             .sort_values(ascending=False)
             .head(1))

# %%
s1 = transacoes.sample(1000)
s1["dtCriacao"] = pd.to_datetime(s1["dtCriacao"])
s1.merge(transacoes)

# %%

