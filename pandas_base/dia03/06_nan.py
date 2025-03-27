# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%
df.dropna(how='any')

# %%
df.dropna(thresh=int(0.3 * df.shape[0]), axis=1)

# %%
df.dropna(subset=["dtCriacao"])

# %%

df = pd.DataFrame(
    {
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "idade": [32, 35, 32, 30, 32, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

media = df["salario"].mean()
std = df["salario"].std()
print("Média:", media)
print("Devio:", std)

df["novo_salario"] = df["salario"].fillna(media)

nova_madia = df["novo_salario"].mean()
novo_std = df["novo_salario"].std()
print("\nMédia:", nova_madia)
print("Devio:", novo_std)

# %%

df