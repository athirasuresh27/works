import pandas as pd
from math import sqrt
df=pd.read_csv("smoking.csv")
column = df.columns
for i in column:
    sum = 0
    if i=="Unnamed: 0":
        continue
    for j in df[i]:
        sum+=j
    mean=sum/len(df)
    var=0
    for el in df[i]:
        value=(el-mean)**2
        var+=value
    variance=var/(len(df)-1)
    print("Standard deviation of",i,"is:\n",sqrt(variance))