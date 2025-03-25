# %%
import pandas as pd

idades = pd.Series([32,34,56,43], name="idades")
nomes = pd.Series(["teo", "nah", "ana", "jose"], name="nomes")

# %%

df = pd.DataFrame()
df["idades"] = idades
df["nomes"] = nomes
df

# %%'
df["nomes"].iloc[2]

# %%

df.iloc[2]["nomes"]

# %%

df["salario"] = [4324,5436,5432,4564]
df

# %%
colunas = ["salario", "nomes"]
df[colunas]

# %%
df[["salario"]]

# %%

df_01 = df[["nomes", "idades"]]

# %%

