import pandas as pd
from math import sqrt
from numpy import Inf
df = pd.read_csv('smoking.csv')
print(df)
global l
def findmean(column):
    sum=0
    l=len(column)
    for i in column:
        sum=sum+i
    mean=sum/l
    return mean
var=0
mean=0
for i in df.columns:
    findmean(df[i])
    print(mean)
    for j in df[i]:
        val=(j-mean)**2
        var+=val
    varience=var/len(df)
    print("Standard deviation", sqrt(varience))




