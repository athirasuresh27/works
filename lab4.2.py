import pandas as pd
df=pd.read_csv("smoking.csv")
df_scaled = df.copy()

for column in df_scaled.columns:
   df_scaled[column] = (df_scaled[column] - df_scaled[column].min()) / (df_scaled[column].max() - df_scaled[column].min())

print("Before Normalize values are::\n",df)
print("=============================================================================")
print("After normalize values are::\n",df_scaled)
