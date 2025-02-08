import pandas

df=pandas.read_csv('f3.csv','r')

print("\n",df)
print("\n",df.values)
print("\n",df.tail(2))
print("\n",df.tail(-2))
print("\n",df.tail())