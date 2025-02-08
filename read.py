import pandas as pd
df=pd.read_csv('f3.csv','r')
print(df)
print(df.values)
df=pd.read_csv('f3.csv','r',index_col=[0])
print(df)
print(df.values)