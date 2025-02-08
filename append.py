import pandas as pd

data=["tisha","anandi","tanvi","khushali"]

df=pd.DataFrame(data,index=['a','b','c','d'])
df.to_csv('f3.csv',mode='a',header=False)