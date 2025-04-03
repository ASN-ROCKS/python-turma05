# %%

import pandas as pd

df_01 = pd.read_csv("../data/homicidios/homicidios_UF.csv", sep=";")
df_02 = pd.read_csv("../data/homicidios/homicidios-negros_UF.csv", sep=";")

# %%
df.set_index(["nome","período"]).unstack()

# %%

df_pivot = df.pivot_table(values="valor", columns="nome", index="período")

# %%
df_pivot.stack().reset_index()

# %%

df_01 = df_01.rename(columns={"valor": "homicidios_geral"})
df_01 = df_01.set_index(["nome", "período"])

df_02 = df_02.rename(columns={"valor": "homicidios_pretos"})
df_02 = df_02.set_index(["nome", "período"])

pd.concat([df_01, df_02], axis=1)

