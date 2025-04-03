# %%

import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%
df = pd.read_sql_table("tb_customers", engine)

# %%

df_transacoes = pd.read_sql_table("tb_order_items", engine)
df_summary_seller = (df_transacoes.groupby("seller_id")["order_id"]
                                  .count()
                                  .reset_index())

# %%

query = """
SELECT seller_id,
       count(*) as qtdeVendas

FROM tb_order_items
GROUP BY seller_id
"""

df_summary = pd.read_sql_query(query, engine)
df_summary