# %%
import pandas as pd
df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.csv')
df
# %%
df_eq25 = df[(  df['mag'] >= 2.5  )]
df_eq25.to_csv('earthquakes_25.csv')
# %%
