import pandas
df=pandas.read_csv('f3.csv')

print(df.loc[:,'name'])
print()

print(df.iloc[:,1])
print()

print(df.loc[:,['name','per']])
print()

print(df.iloc[:,[0,2]])
print()

print(df['name'].values)
print()
print(df['name'])
