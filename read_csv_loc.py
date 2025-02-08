import pandas
df=pandas.read_csv('f3.csv','r',index_col=[0])
print("\n",df)
print("\n",df.values)

print("\n",df.loc[1])
print("\n",df.iloc[0])

print("\n",df.loc[[1]])
print("\n",df.iloc[[0]])

print("\n",df.loc[[1,3,5]])
print("\n",df.iloc[[0,2,4]])