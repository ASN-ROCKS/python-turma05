# %%

import pandas as pd

df = pd.DataFrame(
    {
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "teo" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "idade": [32, 35, 32, 30, 32, 32, 32],
    }
)

df

# %%

df.drop_duplicates(keep='last')

# %%

df.sort_values(by=['nome']).drop_duplicates(subset=["sobrenome"], keep='last')

# %%

df.sort_values(by=['nome']).drop_duplicates(subset=["sobrenome", "idade"], keep='last')
