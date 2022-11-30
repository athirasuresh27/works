import pandas as pd
from math import sqrt
from numpy import Inf
df = pd.read_csv('smoking.csv')
print(df)
a=[]
def findmean(column):
    sum=0
    l=len(column)
    for i in column:
        sum=sum+i
    avg=sum/l
    print(avg)
def findmin(column):
     min=Inf
     for i in column:
         if i<min:
             min=i
     print(min)
def findmax(column):
    max =0
    for i in column:
        if i>max:
            max=i
    print(max)
for i in df.columns:
    findmean(df[i])
    findmin(df[i])
    findmax(df[i])



